from django.conf.urls import include
from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('create_qna/', views.create_qna, name='create_qna'),
    path('solve_qna/<int:qna_pk>', views.solve_qna, name='solve_qna'),
    path('score/<int:score_pk>', views.score, name='score'),
    path('account/', views.account, name='account'),
    path('signup/user_home/', views.user_home, name='user_home'),
    path('share_qna/', views.share_qna, name='share_qna'),
]
