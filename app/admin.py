from django.contrib import admin
from .models import Planet,Qna,Question,Option,Qna_question,Answer,Choice,Score,Distance
# Register your models here.
admin.site.register(Planet)
admin.site.register(Qna)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Qna_question)
admin.site.register(Answer)
admin.site.register(Choice)
admin.site.register(Score)
admin.site.register(Distance)