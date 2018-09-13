# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-13 10:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('migrate', '0008_auto_20180717_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oldsubmission',
            name='status',
            field=models.IntegerField(choices=[(-4, 'Submitted'), (-3, 'Waiting'), (-2, 'Judging'), (-1, 'Wrong answer'), (0, 'Accepted'), (1, 'Time limit exceeded'), (2, 'Idleness limit exceeded'), (3, 'Memory limit exceeded'), (4, 'Runtime error'), (5, 'Denial of judgement'), (6, 'Compilation error'), (7, 'Partial score'), (11, 'Checker error'), (12, 'Pretest passed')], default=-3),
        ),
    ]
