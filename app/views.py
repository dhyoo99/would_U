from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect
from .models import Planet, Qna, Question, Option, Qna_question, Answer, Choice, Score, Distance
from django.contrib.auth.decorators import login_required
from .distance import createDistance


def index(request):
    if request.method == 'GET':
        return render(request, 'planet/index.html')

    if request.method == 'POST':
        return redirect('/')

def account(request):
    return render(request, 'planet/account.html')


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            username = request.POST["username"]
            password = request.POST["password1"]
            planetname = request.POST["planetname"]

            user = User.objects.create_user(username=username, password=password)
            user.planet.name = planetname
            user.save()
            auth.login(request, user)
            return redirect('/app/user_home/', {"user":user})
    return render(request, 'registration/signup.html')

@login_required(login_url='/app/login/login')
def create_qna_home(request):
    questions = Question.objects.all()

    new_qna = Qna.objects.get(
        owner=request.user
    )

    if Qna_question.objects.filter(Qna=new_qna).count() > 0:
        error = '이미 작성완료했습니다'
        return render(request, 'planet/share_qna.html', {'error':error})

    return render(request, 'planet/create_qna_home.html')

@login_required(login_url='/app/login/login')
def create_qna(request):
    questions = Question.objects.all()

    new_qna = Qna.objects.get(
        owner=request.user
    )
    if Qna_question.objects.filter(Qna=new_qna).count() > 0:
        error = '이미 작성완료했습니다'
        return render(request, 'planet/share_qna.html', {'error':error})

    if request.method == 'POST':

        qna_questions = []
        for q in questions:
            qna_question, created = Qna_question.objects.get_or_create(
                Qna=new_qna,
                question=q
            )
            qna_questions.append(qna_question)
        print(qna_questions)

        for pair in qna_questions:
            answer = Option.objects.get(pk=request.POST[f'{pair.question.pk}'])
            a = Answer.objects.create(
                qna_question=pair,
                option=answer
            )
            print(a)

        qna_pk = new_qna.pk
        return redirect('/app/share_qna', qna_pk)  # share_qna로 redirect하게 수정 필요

    return render(request, 'planet/create_qna.html', {'questions': questions})

@login_required(login_url='/app/login/login')
def solve_qna_home(request):
    return render(request, 'planet/solve_qna_home.html')

@login_required(login_url='/app/login/login')
def solve_qna(request, qna_pk):
    qna_to_solve = Qna.objects.get(pk=qna_pk)
    planet_name = Planet.objects.get(user=qna_to_solve.owner).name
    qna_questions = Qna_question.objects.filter(Qna=qna_to_solve)

    # error handling
    error = False
    if request.user.pk == qna_to_solve.owner.pk:
        error = '자신의 문제는 풀수 없어요'
    elif Score.objects.filter(qna=qna_to_solve, user=request.user).count() > 0:
        error = '이미 푼 문제입니다'

    if error:
        return render(request, 'planet/solve_qna.html', {'error': error})

    if request.method == 'POST':
        choices = []
        score_cnt = 0
        for pair in qna_questions:
            choice = Option.objects.get(pk=request.POST[f'{pair.question.pk}'])
            answer = Answer.objects.get(qna_question=pair).option

            if choice == answer:
                isAnswer = True
                score_cnt += 1
            else:
                isAnswer = False

            c = Choice.objects.create(
                qna_question=pair,
                solver=request.user,
                option=choice,
                isAnswer=isAnswer
            )
            choices.append(c)

        # create Score
        score = Score.objects.create(
            user=request.user,
            qna=qna_to_solve,
            score=score_cnt
        )

        return redirect('score', score.pk)
    return render(request, 'planet/solve_qna.html', {'qna_to_solve': qna_to_solve, 'qna_questions': qna_questions, 'planet_name': planet_name})

def user_home(request):
    return render(request, 'planet/user_home.html')

def score(request, score_pk):
    score = Score.objects.get(pk=score_pk)
    d = createDistance(score_pk)
    print(d.distance)
    return render(request, 'planet/score.html', {'score': score})

@login_required(login_url='/app/login/login')
def share_qna(request):
    return render(request, 'planet/share_qna.html')

@login_required(login_url='/app/login/login')
def result_qna(request):
    return render(request, 'planet/result_qna.html')

@login_required(login_url='/app/login/login')
def answer_detail(request):
    return render(request, 'planet/answer_detail.html')