# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-06-02 18:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aroma', '0015_auto_20170602_1837'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aroma',
            old_name='group',
            new_name='groups',
        ),
    ]
