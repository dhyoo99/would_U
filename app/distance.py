from django.contrib.auth.models import User
from .models import Planet, Qna, Question, Option, Qna_question, Answer, Choice, Score, Distance


def createDistance(score_pk):
    score = Score.objects.get(pk=score_pk)
    solver = score.user
    qna_owner = score.qna.owner

    this_planet = Planet.objects.get(user=solver)  # 문제 푼사람
    that_planet = Planet.objects.get(user=qna_owner)  # 문제 낸 사람

    distance = 1000000

    qna_questions = Qna_question.objects.filter(Qna=score.qna)
    for pair in qna_questions:
        choice = Choice.objects.get(qna_question=pair, solver=solver)

        if choice.isAnswer:
            distance -= pair.question.weight * 55555
            # 랜덤한 숫자 가중치에 곱해서 거리 계산
            # 거리계산 logic 수정 필요할듯..?
    new_distance = Distance.objects.create(
        this=this_planet,
        that=that_planet,
        distance=distance
    )

    return new_distance

# 두 planet간 거리로 보여줄 값 계산


def getDistance(planet_pk_1, planet_pk_2):
    planet_1 = Planet.objects.get(pk=planet_pk_1)
    planet_2 = Planet.objects.get(pk=planet_pk_2)

    distance_1to2 = Distance.objects.filter(this=planet_1, that=planet_2)
    distance_2to1 = Distance.objects.filter(this=planet_2, that=planet_1)

    if distance_1to2.count() > 0:
        if distance_2to1.count() > 0:
            result = (distance_1to2[0].distance +
                      distance_2to1[0].distance) / 2
            return result
        else:
            result = distance_1to2[0].distance
            return result
    else:
        if distance_2to1.count() > 0:
            result = distance_2to1[0].distance
            return result
        else:
            default = 1000000
            return default
