from django.db import models
from django.contrib.auth.models import User

class FakeTwitterProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    # symmetricalがFalseとは、自動フォロバはしない、ということ
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)

    def __str__(self):
        return self.user.username


User.fake_twitter_profile = property(lambda u: FakeTwitterProfile.objects.get_or_create(user=u)[0])

