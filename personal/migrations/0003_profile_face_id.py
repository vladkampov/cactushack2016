# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-14 23:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0002_auto_20160514_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='face_id',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]