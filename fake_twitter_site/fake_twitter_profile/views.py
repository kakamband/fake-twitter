from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from fake_twitter_profile.forms import SignupForm, SigninForm
from tweet.forms import TweetForm

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse_lazy
from .models import FakeTwitterProfile


# profileを表示する
def profile(request, username): 
    if request.user.is_authenticated:
        user = User.objects.get(username=username)
        if request.method == 'POST':
            print(50000)
            form = TweetForm(data=request.POST)
            print(666)
            if form.is_valid():
                tweet = form.save(commit=False)
                tweet.user = request.user
                tweet.save()
        
                redirecturl = request.POST.get('redirect', '/')

                return redirect(redirecturl)
        else:
            form = TweetForm()

        return render(request, 'profile.html', {'form': form, 'user': user})
    else:
        return redirect('/')
    


def frontpage(request):
    if request.user.is_authenticated:
        print(66666)
        return redirect('/'+request.user.username+'/')
    else:
        if request.method == 'POST':
            print(669)
            if 'signupform' in request.POST:
                print(334)
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
                print(670)
                signinform = SigninForm(data=request.POST)
                signupform = SignupForm()
                print(671)
                if signupform.is_valid():
                    login(request, signupform.get_user())
                    print(672)
                    return redirect('/')
        else:
            # signupformとsigninformを初期化
            signupform = SignupForm()
            signinform = SigninForm()
            print(668)
        
        return render(request, 'frontpage.html', {'signupform': signupform, 'signinform': signinform})

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

def follows(request, username):
    user = User.objects.get(username=username)
    fake_tweeter_profiles = user.fake_twitter_profile.follows.select_related('user').all()

    return render(request, 'users.html', {'title':'Followers','fake_tweeter_profiles':fake_tweeter_profiles})

def followers(request, username):
    user = User.objects.get(username=username)
    fake_tweeter_profiles = user.fake_twitter_profile.followed_by.select_related('user').all()
    print(fake_tweeter_profiles)

    return render(request, 'users.html', {'title':'Followers', 'fake_tweeter_profiles':fake_tweeter_profiles})



@login_required
def follow(request, username):
    user = User.objects.get(username=username)
    request.user.fake_twitter_profile.follows.add(user.fake_twitter_profile)

    return redirect('/'+user.username+'/')

@login_required
def stopfollow(request, username):

    user = User.objects.get(username=username)
    request.user.fake_twitter_profile.follows.remove(user.fake_twitter_profile)

    return redirect('/'+user.username+'/')




