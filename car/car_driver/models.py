from django.db import models
from car import settings
from django.contrib.auth.models import User, Group
from django.db.models import Q, signals
from django.dispatch import receiver
from django.db.models.signals import post_save
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
Gender_Choices = (
    ('F', 'female'),
    ('M', 'male'),
    ('Both', 'both'),
    ('None', 'non-specified'),
)


class DriverProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    profile_pic = models.ImageField(upload_to='profile_pictures/', blank=True)
    car_picture = models.ImageField(upload_to='pictures/')
    number_plates = models.CharField(max_length=30)
    capacity = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    phone = PhoneNumberField(max_length=30)
    city = models.CharField(max_length=60)
    bio = models.CharField(max_length=140, blank=True)
    gender = models.CharField(
        max_length=30, choices=Gender_Choices, default='None')


User.profile = property(
    lambda u: DriverProfile.objects.get_or_create(user=u)[0])


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        DriverProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


post_save.connect(create_user_profile, sender=User)
