from django.contrib import admin
from fake_twitter_profile.models import FakeTwitterProfile

# Register your models here.
@admin.register(FakeTwitterProfile)
class FakeTwitterProfileAdmin(admin.ModelAdmin):
    pass