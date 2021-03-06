# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-10 13:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('car_driver', '0005_travelplan_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='PickupPoints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('road_name', models.CharField(max_length=140)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='travelplan',
            name='road',
        ),
        migrations.AddField(
            model_name='travelplan',
            name='roads',
            field=models.ManyToManyField(related_name='pickup', to='car_driver.PickupPoints'),
        ),
    ]
