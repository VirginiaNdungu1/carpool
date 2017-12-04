from django import forms
from .models import User, Group, RiderProfile


class RiderForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username',)


class RiderProfileForm(forms.ModelForm):
    class Meta:
        model = RiderProfile
        fields = ('gender', 'bio')
