from django.conf.urls import include
from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('create_qna/', views.create_qna, name='create_qna'),
    path('solve_qna/<int:qna_pk>/solve_login/', views.solve_login, name='solve_login'),
    path('solve_qna/<int:qna_pk>/solve_signup/', views.solve_signup, name='solve_signup'),
    path('score/<int:score_pk>/', views.score, name='score'),

    path('user_home/', views.user_home, name='user_home'), 

    path('create_qna_home/', views.create_qna_home, name='create_qna_home'),
    path('create_qna/', views.create_qna, name='create_qna'),
    path('share_qna/', views.share_qna, name='share_qna'),

    path('solve_qna/<int:qna_pk>', views.solve_qna, name='solve_qna'),
    path('score/<int:score_pk>', views.score, name='score'),
    path('friend_list/<int:user_pk>', views.friend_list, name='friend_list'),
    path('answer_detail/', views.answer_detail, name='answer_detail'), 
    
    path('account/', views.account, name='account'),
    path('user_home/<int:user_pk>/', views.user_home, name='user_home'),
    path('share_qna/', views.share_qna, name='share_qna'),

  # friend_list의 결과가져옴
    path('result', views.result, name='result'),
]
