from django.contrib.auth.models import User
from .models import Planet, Qna, Question, Option, Qna_question, Answer, Choice, Score, Distance

# score 계산시 Distance 생성


def createDistance(score_pk):
    score = Score.objects.get(pk=score_pk)
    solver = score.user
    qna_owner = score.qna.owner

    this_planet = Planet.objects.get(user=solver)  # 문제 푼사람
    that_planet = Planet.objects.get(user=qna_owner)  # 문제 낸 사람


    qna_questions = Qna_question.objects.filter(Qna=score.qna)
    weight = 0

    for pair in qna_questions:
        choice = Choice.objects.get(qna_question=pair, solver=solver)

        if choice.isAnswer:
            weight += pair.question.weight

    option = {
        0 : 2147483647, 
        1 : 1894798124, 
        2 : 894987833, 
        3 : 624192878, 
        4 : 489791256, 
        5 : 123894567, 
        6 : 73209849, 
        7 : 45289372, 
        8 : 5238972, 
        9 : 3624355, 
        10 : 61878, 
        11 : 29488, 
        12 : 3987, 
        13 : 4874, 
        14 : 909, 
        15 : 122, 
        16 : 77, 
        17 : 11, 
        18 : 7 
        }

    new_distance = Distance.objects.create(
        this=this_planet,
        that=that_planet,
        distance = option[weight]
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
            default = 2147483647
            return default
