from django import forms
from .models import User, Group, DriverProfile, TravelPlan


class DriverForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')


class DriverProfileForm(forms.ModelForm):

    class Meta:
        model = DriverProfile
        exclude = ['user', 'bio']


class TravelPlanForm(form.ModelForm):
    class Meta:
        model = TravelPlan
        exclude = ['name', 'created_at']
