# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-18 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aroma', '0016_auto_20170602_1844'),
    ]

    operations = [
        migrations.AddField(
            model_name='aroma',
            name='slug',
            field=models.SlugField(blank=True, max_length=256, null=True),
        ),
    ]
