from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.

class Planet(models.Model):
    owner = models.OneToOneField(User, on_delete= models.CASCADE, primary_key= True)
    name = models.CharField(max_length=100)
    #img_src = models.TextField()

class QnA(models.Model):
    owner = models.OneToOneField(User, on_delete = models.CASCADE, related_name = 'QnA')

#질문 목록 data
class Question(models.Model):
    content = models.TextField()

#질문에 대한 option data
class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name= 'options')
    content = models.CharField(max_length=200)

#QnA와 그 안에 포함된 Question의 관계 나타냄.
class QnA_question(models.Model):
    QnA = models.ForeignKey(QnA, on_delete = models.CASCADE, related_name= 'QnA_questions')
    question = models.ForeignKey(Question, on_delete = models.CASCADE, related_name='QnA_questions')
    weight = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(3)]) #문제의 점수 가중치 1~3

# QnA owner의 초기 정답
class Answer(models.Model):
    qna_question = models.OneToOneField(QnA_question, on_delete=models.CASCADE, related_name = 'answer')
    answerer = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'answers')
    option = models.ForeignKey(Option, on_delete = models.CASCADE, related_name = 'answers')

#문제 푸는 user의 choice
class Choice(models.Model):
    qna_question = models.ForeignKey(QnA_question, on_delete = models.CASCADE, related_name= 'choices')
    solver = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'choices')
    option = models.ForeignKey(Option, on_delete = models.CASCADE, related_name = 'choices')
    isAnswer = models.BooleanField(default= False)

# 각 QnA에 대한 user의 점수
class Score(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'scores')
    QnA = models.ForeignKey(QnA, on_delete = models.CASCADE, related_name = 'scores')
    score = models.IntegerField()

#각 행성간 거리
class Distance(models.Model):
    this = models.ForeignKey(Planet, on_delete=models.CASCADE, related_name= 'distances')
    that = models.ForeignKey(Planet, on_delete=models.CASCADE, related_name= 'that_distances')
    distance = models.IntegerField()