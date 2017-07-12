from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models

from tag.models import TaggedItem


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
    created_at = models.DateTimeField(auto_now_add=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    def __str__(self):
        return "User %s(%d) %s %s(%d)" % (self.user.username, self.user.id, self.get_activity_type_display(),
                                          self.content_type, self.object_id)


class Comment(models.Model):
    LONGEVITY_TYPES = (('S', 'Сильная'), ('M', 'Средняя'), ('W', 'Слабая'),)
    SILLAGE_TYPES = (('S', 'Сильный'), ('M', 'Средний'), ('W', 'Близко к коже'),)
    SEASON_TYPES = (('SP', 'Весна'), ('SM', 'Лето'), ('A', 'Осень'), ('W', 'Зима'), ('E', 'Любое'))
    IMPRESSION_TYPES = (('F', 'Люблю'), ('L', 'Нравится'), ('N', 'Нейтральное'), ('D', 'Не нравится'),)
    user = models.ForeignKey(User)
    aroma = models.ForeignKey('aroma.Aroma', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=True)
    text = models.TextField()
    votes = GenericRelation(Activity)
    longevity = models.CharField(max_length=1, choices=LONGEVITY_TYPES, blank=True, null=True)
    sillage = models.CharField(max_length=1, choices=SILLAGE_TYPES, blank=True, null=True)
    season = models.CharField(max_length=2, choices=SEASON_TYPES, blank=True, null=True)
    impression = models.CharField(max_length=1, choices=IMPRESSION_TYPES)
    rating = models.SmallIntegerField(default=0)
    taggeditems = GenericRelation(TaggedItem)

    def __str__(self):
        return self.text
