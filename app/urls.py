from django.conf.urls import include
from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),

    path('create_qna/', views.create_qna, name='create_qna'),
    path('solve_qna/<int:qna_pk>', views.solve_qna, name='solve_qna'),
    path('score/<int:score_pk>', views.score, name='score'),
    path('friend_list/<int:user_pk>', views.friend_list, name='friend_list'),

    # friend_list의 결과가져옴
    path('result', views.result, name='result'),
]
