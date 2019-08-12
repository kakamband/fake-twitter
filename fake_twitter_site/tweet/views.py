from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Tweet, Fav

def feed(request):
    userids = []
    for id in request.user.fake_twitter_profile.follows.all():
        userids.append(id.id)
    
    userids.append(request.user.id)
    print(userids)
    tweets = Tweet.objects.filter(user_id__in=userids)[0:25]

    return render(request, 'feed.html',{'tweets':tweets})

@login_required
def fav(request, tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)
    is_fav = Fav.objects.filter(fav_user_id=request.user.id).filter(favtweet=tweet).count()

    favs = models.ManyToManyField('self', related_name='fav_number', symmetrical=False)

    # unfav
    if is_fav > 0:
        fav_num = Fav.objects.create(fav_user_id=request.user.id, favtweet=tweet,related='fav_number')
        tweet.fav_num -= 1
        tweet.save()

    # fav
    else :
        fav_num = Fav.objects.create(fav_user_id=request.user.id, favtweet=tweet,related='fav_number')
        tweet.fav_num += 1
        tweet.save()
    
    return redirect('/'+user.username+'/')