from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from aroma.models import Aroma
from activity.models import Activity, Comment


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account')

    @receiver(post_save, sender=User)
    def save_user_account(sender, instance, **kwargs):
        if not hasattr(instance, 'account'):
            Account.objects.create(user=instance)

    def get_full_name(self):
        return self.user.get_full_name() or self.user.username

    def get_short_name(self):
        return self.user.get_short_name() or self.user.username

    def __str__(self):
        return self.get_full_name()

    def get_absolute_url(self):
        return reverse('profile-public', kwargs={'username': self.user.username})

    @property
    def num_comments(self):
        return Comment.objects.filter(user_id=self.user.id).count()

    @property
    def num_favorites(self):
        return Aroma.objects.filter(marks__user_id=self.user.id, marks__activity_type=Activity.FAVORITE).count()

    @property
    def num_likes(self):
        return Aroma.objects.filter(marks__user_id=self.user.id, marks__activity_type=Activity.LIKE).count()
