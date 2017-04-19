from __future__ import unicode_literals

from django.db import models


class Group(models.Model):
    group_id = models.AutoField(primary_key=True)
    parent_id = models.IntegerField()
    title = models.CharField(max_length=200)
