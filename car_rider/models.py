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


class RiderProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='rider_profile', unique=True)
    picture = models.ImageField(upload_to='user_pics/', blank=True)
    phone = PhoneNumberField(max_length=30)
    bio = models.CharField(max_length=500, blank=True)
    gender = models.CharField(
        max_length=30, choices=Gender_Choices, default='None', blank=True)

    @staticmethod
    def is_rider(instance):
        return instance.groups.filter(name='riders').exists()


User.rider_profile = property(
    lambda u: RiderProfile.objects.get_or_create(user=u)[0])


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        RiderProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.rider_profile.save()


post_save.connect(create_user_profile, sender=User)


class TravelRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=140)
    desired_pickup = models.CharField(max_length=140)
    current_location = models.CharField(max_length=140)
    endpoint = models.CharField(max_length=140)
    capacity = models.IntegerField()
    pub_date = models.DateTimeField(auto_now_add=True)
    travel_plan = models.ForeignKey(
        'car_driver.TravelPlan', on_delete=models.CASCADE)

    def __str__(self):
        self.name
