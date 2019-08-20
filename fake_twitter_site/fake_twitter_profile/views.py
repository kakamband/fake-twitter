from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from tweet.models import Tweet, Fav
from tweet.forms import TweetForm

 
# profileを表示する
def profile(request, username): 
    if request.user.is_authenticated:
        user = User.objects.get(username=username)
        if request.method == 'POST':
            form = TweetForm(data=request.POST)
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

    return render(request, 'users.html', {'title':'Follows','fake_tweeter_profiles':fake_tweeter_profiles})

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


