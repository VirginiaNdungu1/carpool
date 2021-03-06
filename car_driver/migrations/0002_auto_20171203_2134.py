# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 21:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_driver', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driverprofile',
            name='car_picture',
            field=models.ImageField(blank=True, upload_to='pictures/'),
        ),
        migrations.AlterField(
            model_name='driverprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='profile_pictures/'),
        ),
    ]
