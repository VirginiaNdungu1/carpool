# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-10 12:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_driver', '0004_travelplan'),
    ]

    operations = [
        migrations.AddField(
            model_name='travelplan',
            name='name',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
