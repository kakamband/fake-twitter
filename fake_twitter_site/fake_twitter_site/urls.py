from django.urls import path
from django.contrib import admin
from tweet.views import feed
from fake_twitter_profile.views import frontpage, signout, profile, follows, followers, follow, stopfollow, signin, fav

urlpatterns = [
    path('admin/',admin.site.urls)
]
urlpatterns += [
  path('', frontpage, name='frontpage'),
  path('feed/', feed, name='feed'),
  path('signout/', signout, name='signout'),
  path('signin/', signin, name='signin'),
  path('<str:username>/follows/',follows,name='follows'),
  path('<str:username>/followers/',followers,name='followers'),
  path('<str:username>/follow/',follow,name='follow'),
  path('<str:username>/stopfollow/',stopfollow,name='stopfollow'),
  path('<str:tweet_id>/fav/',fav,name='fav'),
  path('<str:username>/',profile,name='profile'),
]