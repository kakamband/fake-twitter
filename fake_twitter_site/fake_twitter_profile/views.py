from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from tweet.forms import TweetForm


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


