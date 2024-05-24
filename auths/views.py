from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from app.models import UserToken

def register_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST['email']
        
        user = User.objects.create(username=username, password=password)
        

        # user = authenticate(request, username=username, password=password)
        login(request, user)
        return redirect("test")   
    return render(request, 'core/register.html',{})

def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('test')
        else:
            return redirect('login_user')
    return render(request, 'core/login.html', {})

def logout_user(request):
    logout(request)
    return redirect('home')


def check_username(request):
    username = request.POST.get('username')
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse('<p id="username-error" class="error" >This Username Already Exists</p>')
    else:
        return HttpResponse('<p id="username-error" class="success">This Username is Available</p>')
    
def check_email(request):
    email = request.POST.get('email')
    if get_user_model().objects.filter(email=email).exists():
        return HttpResponse('<p class="error">This Email Already Used </p>')
    else:
        return HttpResponse('<p class="success">This  Available</p>')
    
def check_password(request):
    password = request.POST.get('password')
    password1 = request.POST.get('password1')
    if password == password1:
        return HttpResponse('<p class="success">Password matched</p>')
    else:
        return HttpResponse('<p class="error">Password dont match... </p>')        
