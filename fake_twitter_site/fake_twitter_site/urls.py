from django.urls import path

from tweet.views import feed
from fake_twitter_profile.views import frontpage, signout, profile

urlpatterns = [
  path('', frontpage, name='frontpage'),
  path('feed/', feed, name='feed'),
  path('signout/', signout, name='signout'),
  # ユーザー名に対応するurlへのリクエストが来た場合にprofileを表示する
  path('<str:username>/',profile,name='profile'),
]