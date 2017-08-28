# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-28 18:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('aroma', '0020_auto_20170816_1227'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('price', models.IntegerField()),
                ('link', models.URLField()),
                ('item_id', models.IntegerField()),
                ('partner_id', models.SmallIntegerField(default=1)),
                ('name', models.CharField(max_length=200)),
                ('aroma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aroma.Aroma')),
            ],
        ),
    ]
