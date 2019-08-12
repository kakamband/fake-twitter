from django.shortcuts import render

from .models import Tweet

def feed(request):
    userids = []
    for id in request.user.fake_twitter_profile.follows.all():
        userids.append(id.id)
    
    userids.append(request.user.id)
    print(userids)
    tweets = Tweet.objects.filter(user_id__in=userids)[0:25]

    return render(request, 'feed.html',{'tweets':tweets})
