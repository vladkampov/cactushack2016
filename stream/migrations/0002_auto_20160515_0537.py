# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-15 05:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stream',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='personal.Profile'),
        ),
    ]