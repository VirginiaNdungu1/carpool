from django import forms
from .models import User, Group, DriverProfile, TravelPlan, PickupPoints


class DriverForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')


class DriverProfileForm(forms.ModelForm):

    class Meta:
        model = DriverProfile
        exclude = ['user', 'bio']


class TravelPlanForm(forms.ModelForm):
    class Meta:
        model = TravelPlan
        exclude = ['created_at', 'user']


class PickupPointsForm(forms.ModelForm):
    class Meta:
        model = PickupPoints
        exclude = ['user']
