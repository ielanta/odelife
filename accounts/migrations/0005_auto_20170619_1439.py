# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 14:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20170618_1219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='user',
        ),
        migrations.DeleteModel(
            name='Activity',
        ),
    ]
