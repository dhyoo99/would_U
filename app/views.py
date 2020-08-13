from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect

# Create your views here.

def signup(request):
    if request.method  == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(userID=request.POST['userID'], password=request.POST['password1'], planetname=request.POST['planetname'])
            auth.login(request, user)
            return redirect('/feeds')
	return render(request, 'accounts/signup.html')
