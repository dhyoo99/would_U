from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

class Planet(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, primary_key= True)
    name = models.CharField(max_length=100)
    #img_src = models.TextField()

    @receiver(post_save, sender=User)
    def create_user_planet(sender, instance, created, **kwargs):  
      if created:
        Planet.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_planet(sender, instance, **kwargs):  
        instance.planet.save()

class Qna(models.Model):
    owner = models.OneToOneField(User, on_delete = models.CASCADE, related_name = 'Qna')

    def __str__(self):
        return self.owner.username
        
#질문 목록 data
class Question(models.Model):
    WEIGHT = ((1,1),(2,2),(3,3))

    content = models.TextField()
    weight = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(3)], choices=WEIGHT) #문제의 점수 가중치 1~3

    def __str__(self):
        return self.content

#질문에 대한 option data
class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name= 'options')
    content = models.CharField(max_length=200)
    def __str__(self):
        return self.content
     

#QnA와 그 안에 포함된 Question의 관계 나타냄.
class Qna_question(models.Model):
    Qna = models.ForeignKey(Qna, on_delete = models.CASCADE, related_name= 'Qna_questions')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name = 'Qna_questions')

    def __str__(self):
        return self.Qna.owner.username + '/' + self.question.content
     
# QnA owner의 초기 정답
class Answer(models.Model):
    qna_question = models.ForeignKey(Qna_question, on_delete=models.CASCADE, related_name = 'answers')    
    option = models.ForeignKey(Option, on_delete = models.CASCADE, related_name = 'answers')



#문제 푸는 user의 choice
class Choice(models.Model):
    qna_question = models.ForeignKey(Qna_question, on_delete = models.CASCADE, related_name= 'choices')
    solver = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'choices')

    option = models.ForeignKey(Option, on_delete = models.CASCADE, related_name = 'choices')
    isAnswer = models.BooleanField(default= False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['qna_question', 'solver'], name= 'unique_choice')
        ]

# 각 QnA에 대한 user의 점수
class Score(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'scores')
    qna = models.ForeignKey(Qna, on_delete = models.CASCADE, related_name = 'scores')
    score = models.IntegerField()

    def __str__(self):
        return self.user.usrname + '/' + self.qna.owner.username
     
#각 행성간 거리
class Distance(models.Model):
    this = models.ForeignKey(Planet, on_delete=models.CASCADE, related_name= 'distances')
    that = models.ForeignKey(Planet, on_delete=models.CASCADE, related_name= 'that_distances')
    distance = models.IntegerField()

    def __str__(self):
        return self.this.name + '/' + self.that.name
     
