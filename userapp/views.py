from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import *
from django.contrib import messages



def registerview(request):
    if request.method == "POST" and request.POST.get('p') == request.POST.get('cp'):
        username = request.POST.get('l')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken')
        else:
            User.objects.create_user(
                username=username,
                password=request.POST.get('p')
            )
            return redirect('/user/login/')
    return render(request, 'register.html')


def loginview(request):
    if request.method == 'POST':
        user = authenticate(
            username=request.POST.get('l'),
            password=request.POST.get('p'),
        )
        if user is None:
            return redirect("/user/register/")
        login(request, user)
        return redirect('/')
    return render(request, 'login.html')

def logoutview(request):
    logout(request)
    return redirect('/user/login/')