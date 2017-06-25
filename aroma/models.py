from __future__ import unicode_literals

from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.text import slugify
from django.urls import reverse

from activity.models import Activity
from django.conf import settings


class Note(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, unique=True)
    pic = models.ImageField(upload_to='notes/', blank=True, null=True)

    def __str__(self):
        return self.title


class Group(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, blank=True, unique=True)

    def __str__(self):
        return self.title


class Nose(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)
    biography = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, unique=True)
    website = models.URLField(blank=True)
    logo = models.ImageField(upload_to='brands/', blank=True, null=True)

    def __str__(self):
        return self.title


class Aroma(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    pic = models.ImageField(upload_to='aromas/', blank=True, null=True)
    guise = models.ImageField(upload_to='guises/', blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    gender = models.CharField(choices=settings.GENDER_CHOICES, default='u', max_length=1)
    description = models.TextField(blank=True)
    groups = models.ManyToManyField(Group, blank=True)
    brand = models.ForeignKey(Brand)
    noses = models.ManyToManyField(Nose, blank=True)
    notes = models.ManyToManyField(Note, through='CategoryNotes', related_name='notes', blank=True)
    is_public = models.BooleanField(default=False)
    marks = GenericRelation(Activity)
    slug = models.SlugField(max_length=256, blank=True, null=True)


    class Meta:
        unique_together = ('title', 'brand', 'gender')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('aroma-detail', kwargs={'slug': self.slug})

    def get_mark_by_type(self, activity_type, user):
        mark = self.marks.filter(activity_type=activity_type, user_id=user.id).first()
        if mark:
            return mark.id
        return mark

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify('-'.join([self.brand.title, self.title, self.gender]))[:256]
        super(Aroma, self).save(*args, **kwargs)

    @property
    def comments_counter(self):
        return self.comment_set.count()


class AromaCounter(models.Model):
    aroma = models.ForeignKey(Aroma, on_delete=models.CASCADE)
    num_comments = models.IntegerField(blank=True, null=True)
    num_views = models.IntegerField(blank=True, null=True)


class CategoryNotes(models.Model):
    TOP_NOTES = 0
    MIDDLE_NOTES = 1
    BASE_NOTES = 2
    GENERAL_NOTES = 3
    CATEGORY_CHOICES = (
        (TOP_NOTES, 'top_notes'),
        (MIDDLE_NOTES, 'middle_notes'),
        (BASE_NOTES, 'base_notes'),
        (GENERAL_NOTES, 'general_notes'),
    )
    aroma = models.ForeignKey(Aroma, on_delete=models.CASCADE)
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    category = models.SmallIntegerField(choices=CATEGORY_CHOICES)
