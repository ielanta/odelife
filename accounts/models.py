from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from aroma.models import Aroma


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account')
    favorites = models.ManyToManyField(Aroma, blank=True, related_name='favorites')
    collection = models.ManyToManyField(Aroma, blank=True, related_name='collection')

    @receiver(post_save, sender=User)
    def save_user_account(sender, instance, **kwargs):
        if not hasattr(instance, 'account'):
            Account.objects.create(user=instance)

    def get_full_name(self):
        return self.user.get_full_name() or self.user.username

    def get_short_name(self):
        return self.user.get_short_name() or self.user.username
