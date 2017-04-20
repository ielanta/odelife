from __future__ import unicode_literals

from django.db import models
from core.settings import GENDER_CHOICES


class Note(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    pic = models.URLField(blank=True)


class Group(models.Model):
    id = models.AutoField(primary_key=True)
    parent_id = models.IntegerField()
    title = models.CharField(max_length=200, blank=True)


class Nose(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    biography = models.TextField(blank=True)


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    website = models.URLField(blank=True)
    logo = models.URLField(blank=True)


class Aroma(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    pic = models.URLField(blank=True)
    year = models.IntegerField(blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, default='u', max_length=1)
    description = models.TextField(blank=True)
    group = models.ForeignKey(Group)
    brand = models.ForeignKey(Brand)
    notes = models.ManyToManyField(Note)
    noses = models.ManyToManyField(Nose)
