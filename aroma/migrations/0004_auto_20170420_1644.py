# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-04-20 16:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aroma', '0003_auto_20170420_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='parent_id',
            field=models.IntegerField(blank=True),
        ),
    ]
