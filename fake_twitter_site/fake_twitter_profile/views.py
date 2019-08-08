from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from fake_twitter_profile.forms import SignupForm, SigninForm
from tweet.forms import TweetForm


def signout(request):
    logout(request)
    return redirect('/')


# profileを表示する
def profile(request, username):
    if request.user.is_authenticated:
        user = User.objects.get(username=username)

        if request.method == 'POST':
            form = TweetForm(data=request.POST)

            if form.is_valid():
                # formを有効にしつつも、データベースには追加しない
                tweet = form.save(commit=False)
                # authenticateしたユーザーを追加
                tweet.user = request.user
                tweet.save()

                redirecturl = request.POST.get('redirect','/')

                return redirect(redirecturl)
            else:
                form = TweetForm()

            return render(request, 'profile.html',{'form':form,'user':user})
        else:
            return redirect('/')
    


def frontpage(request):
    if request.user.is_authenticated:
        print(66666)
        return redirect('/'+request.user.username+'/') # Change this line
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
            signupform = SignupForm()
            signinform = SigninForm()
        
        return render(request, 'frontpage.html', {'signupform': signupform, 'signinform': signinform})
