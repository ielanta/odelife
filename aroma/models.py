from __future__ import unicode_literals

from django.db import models
from core.settings import GENDER_CHOICES


class Note(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, unique=True)
    pic = models.ImageField(upload_to='notes/', blank=True, null=True)

    def __str__(self):
        return self.title


class Group(models.Model):
    id = models.AutoField(primary_key=True)
    parent = models.ForeignKey('self', blank=True, null=True)
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
    year = models.IntegerField(blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, default='u', max_length=1)
    description = models.TextField(blank=True)
    group = models.ForeignKey(Group)
    brand = models.ForeignKey(Brand)
    noses = models.ManyToManyField(Nose, blank=True)
    notes = models.ManyToManyField(Note, through='CategoryNotes', related_name='notes', blank=True)
    is_public = models.BooleanField(default=False)

    class Meta:
        unique_together = ('title', 'brand', 'gender')

    def __str__(self):
        return self.title


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



