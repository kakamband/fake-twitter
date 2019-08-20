from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout

def signin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/{0}/'.format(user.username))
    return redirect('/')

def signout(request):
    logout(request)
    return redirect('/')