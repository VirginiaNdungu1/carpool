from django import forms
from .models import User, Group, DriverProfile


class DriverForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')


class DriverProfileForm(forms.ModelForm):

    class Meta:
        model = DriverProfile
        exclude = ['user', 'bio']
