from django.contrib import admin
from .models import Planet,QnA,Question,Option,QnA_question,Answer,Choice,Score,Distance
# Register your models here.
admin.site.register(Planet)
admin.site.register(QnA)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(QnA_question)
admin.site.register(Answer)
admin.site.register(Choice)
admin.site.register(Score)
admin.site.register(Distance)