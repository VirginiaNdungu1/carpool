# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 17:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RiderProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, upload_to='pictures/')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=30)),
                ('bio', models.CharField(blank=True, max_length=500)),
                ('gender', models.CharField(blank=True, choices=[('F', 'female'), ('M', 'male'), ('Both', 'both'), ('None', 'non-specified')], default='None', max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='rider_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]