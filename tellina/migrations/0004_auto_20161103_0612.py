# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-03 06:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tellina', '0003_auto_20161102_0609'),
    ]

    operations = [
        migrations.RenameField(
            model_name='translation',
            old_name='pred_CMD',
            new_name='pred_cmd',
        ),
        migrations.AlterField(
            model_name='nlrequest',
            name='sub_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='translation',
            name='score',
            field=models.FloatField(),
        ),
    ]
