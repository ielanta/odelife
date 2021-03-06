# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-05-04 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aroma', '0010_auto_20170503_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aroma',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='aromas/'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='brands/'),
        ),
        migrations.AlterField(
            model_name='note',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='notes/'),
        ),
    ]
