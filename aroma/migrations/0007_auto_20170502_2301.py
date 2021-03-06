# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-05-02 23:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aroma', '0006_auto_20170420_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='aroma',
            name='base_notes',
            field=models.ManyToManyField(blank=True, related_name='base_notes', to='aroma.Note'),
        ),
        migrations.AddField(
            model_name='aroma',
            name='middle_notes',
            field=models.ManyToManyField(blank=True, related_name='middle_notes', to='aroma.Note'),
        ),
        migrations.AddField(
            model_name='aroma',
            name='top_notes',
            field=models.ManyToManyField(blank=True, related_name='top_notes', to='aroma.Note'),
        ),
        migrations.AlterField(
            model_name='aroma',
            name='gender',
            field=models.CharField(choices=[(b'f', b'\xd0\xb6\xd0\xb5\xd0\xbd\xd1\x81\xd0\xba\xd0\xb8\xd0\xb9'), (b'm', b'\xd0\xbc\xd1\x83\xd0\xb6\xd1\x81\xd0\xba\xd0\xbe\xd0\xb9'), (b'u', b'\xd1\x83\xd0\xbd\xd0\xb8\xd1\x81\xd0\xb5\xd0\xba\xd1\x81')], default='u', max_length=1),
        ),
        migrations.AlterField(
            model_name='aroma',
            name='noses',
            field=models.ManyToManyField(blank=True, to='aroma.Nose'),
        ),
        migrations.AlterField(
            model_name='aroma',
            name='notes',
            field=models.ManyToManyField(blank=True, related_name='notes', to='aroma.Note'),
        ),
    ]
