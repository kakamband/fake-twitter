from django.contrib import admin
from fake_twitter_profile.models import FakeTwitterProfile

@admin.register(FakeTwitterProfile)
class FakeTwitterProfileAdmin(admin.ModelAdmin):
    pass