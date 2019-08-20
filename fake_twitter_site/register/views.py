from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from tweet.forms import TweetForm
from register.forms import SignupForm, SigninForm


def frontpage(request):
    if request.user.is_authenticated:
        return redirect('/'+request.user.username+'/')
    else:
        if request.method == 'POST':
            if 'signupform' in request.POST:
                signupform = SignupForm(data=request.POST)
                signinform = SigninForm()
        
                if signupform.is_valid():
                    username = signupform.cleaned_data['username']
                    password = signupform.cleaned_data['password1']
                    signupform.save()
                    user = authenticate(username=username, password=password)
                    login(request, user)
                    return redirect('/')
            else:
                signinform = SigninForm(data=request.POST)
                signupform = SignupForm()
                if signupform.is_valid():
                    login(request, signupform.get_user())
                    return redirect('/')
        else:
            # signupformとsigninformを初期化
            signupform = SignupForm()
            signinform = SigninForm()
        
        return render(request, 'frontpage.html', {'signupform': signupform, 'signinform': signinform})
