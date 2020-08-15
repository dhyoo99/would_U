from django.conf.urls import include
from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),

    path('user_home/', views.user_home, name='user_home'), 


    path('create_qna_home/', views.create_qna_home, name='create_qna_home'),
    path('create_qna/', views.create_qna, name='create_qna'),
    path('share_qna/', views.share_qna, name='share_qna'),

    path('solve_qna_home/', views.solve_qna_home, name='solve_qna_home'),
    path('solve_qna/<int:qna_pk>', views.solve_qna, name='solve_qna'),
    path('score/<int:score_pk>', views.score, name='score'),

    path('result_qna/', views.result_qna, name='result_qna'), 
    path('answer_detail/', views.answer_detail, name='answer_detail'), 
    
    path('account/', views.account, name='account'),
    path('signup/user_home/', views.user_home, name='user_home'),
    path('share_qna/', views.share_qna, name='share_qna'),

]
