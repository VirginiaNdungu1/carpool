# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 22:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_driver', '0002_auto_20171203_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driverprofile',
            name='car_picture',
            field=models.ImageField(upload_to='pictures/'),
        ),
    ]
