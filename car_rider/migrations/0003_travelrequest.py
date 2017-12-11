# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-11 11:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car_driver', '0006_auto_20171210_1302'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('car_rider', '0002_auto_20171203_2254'),
    ]

    operations = [
        migrations.CreateModel(
            name='TravelRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('desired_pickup', models.CharField(max_length=140)),
                ('current_location', models.CharField(max_length=140)),
                ('endpoint', models.CharField(max_length=140)),
                ('capacity', models.IntegerField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('travel_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_driver.TravelPlan')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]