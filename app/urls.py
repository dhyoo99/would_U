from django.conf.urls import include
from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('create_qna/', views.create_qna, name='create_qna'),
    path('solve_qna/<int:qna_pk>/solve_login/',
         views.solve_login, name='solve_login'),
    path('solve_qna/<int:qna_pk>/solve_signup/',
         views.solve_signup, name='solve_signup'),
    path('score/<int:score_pk>/', views.score, name='score'),

    path('user_home/', views.user_home, name='user_home'),

    path('create_qna_home/', views.create_qna_home, name='create_qna_home'),
    path('share_qna/<int:qna_pk>', views.share_qna, name='share_qna'),


    path('answer_detail/<int:score_pk>',
         views.answer_detail, name='answer_detail'),
    path('account/', views.account, name='account'),
    path('user_home/<int:user_pk>/', views.user_home, name='user_home'),
    
    path('rank/<int:user_pk>', views.rank, name='rank'),
    path('friend_planet/<int:user_pk>',
         views.friend_planet, name='friend_planet'),

    # friend_list의 결과가져옴
    path('result', views.result, name='result'),
]