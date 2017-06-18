from django.db import models
from django.db.models.signals import post_save
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.dispatch import receiver


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


class Activity(models.Model):
    FAVORITE = 'F'
    LIKE = 'L'
    UP_VOTE = 'U'
    DOWN_VOTE = 'D'
    ACTIVITY_TYPES = (
        (FAVORITE, 'Favorite'),
        (LIKE, 'Like'),
        (UP_VOTE, 'Up Vote'),
        (DOWN_VOTE, 'Down Vote'),
    )

    user = models.ForeignKey(User)
    activity_type = models.CharField(max_length=1, choices=ACTIVITY_TYPES)
    date = models.DateTimeField(auto_now_add=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    def __str__(self):
        return "User %s(%d) %s %s(%d)" % (self.user.username, self.user.id, self.get_activity_type_display(),
                                          self.content_type, self.object_id)
