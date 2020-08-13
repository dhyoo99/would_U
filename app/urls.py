from django.conf.urls import include
from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
]
