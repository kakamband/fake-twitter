from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


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

