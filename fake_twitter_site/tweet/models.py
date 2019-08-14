from django.db import models
from django.contrib.auth.models import User

class Tweet(models.Model):
    user = models.ForeignKey(User, related_name='tweets', on_delete=models.DO_NOTHING)
    body = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    fav_num = models.IntegerField(default=0)

    class Meta:
        # タイムラインを新着順にする
        ordering = ('-created_at',)

class Fav(models.Model):
    favtweet = models.ForeignKey(Tweet, on_delete=models.DO_NOTHING,related_name='fav_number')
    fav_user = models.ForeignKey(User,on_delete=models.DO_NOTHING)