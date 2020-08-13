from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect
from .models import Planet

def index(request):
    if request.method == 'GET':
        return render(request, 'planet/index.html')

    if request.method == 'POST':
        return redirect('/')

def signup(request):
    if request.method  == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            username = request.POST["username"]
            password = request.POST["password1"]
            planetname = request.POST["planetname"]

            user = User.objects.create_user(username=username, password=password)
            user.save()
            auth.login(request, user)
            return redirect('/app/')
    return render(request, 'account/signup.html')

