from django.conf.urls import include
from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    #장고 로그인 기능으로 대체
    # path('/login/', views.login, name='login'),
    # path('/logout/', views.logout, name='logout'),
]