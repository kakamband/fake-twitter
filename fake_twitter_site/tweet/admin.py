from django.contrib import admin
from tweet.models import Fav, Tweet

# Register your models here.
@admin.register(Fav)
class FavAdmin(admin.ModelAdmin):
    pass

@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    pass