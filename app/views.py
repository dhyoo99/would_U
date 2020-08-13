from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def index(request):

    return render(request, 'account/index.html')

def signup(request):
    if request.method  == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(userID=request.POST['userID'], password=request.POST['password1'], planetname=request.POST['planetname'])
            auth.login(request, user)
            return redirect('/feeds')
            
    return render(request, 'account/signup.html')
