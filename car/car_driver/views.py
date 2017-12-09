from django.shortcuts import render, redirect
from car import settings
from django.db import transaction
from django.contrib import messages
from .models import DriverProfile
from django.contrib.auth.decorators import login_required
from .forms import DriverForm, DriverProfileForm
from django.contrib.auth.models import User, Group
# Create your views here.


def drive(request):
    return render(request, 'drive.html')


@login_required(login_url='/accounts/login/')
@transaction.atomic
def activateDriver(request):
    instance = request.user
    if request.method == 'POST':
        form = DriverForm(request.POST, request.FILES, instance=request.user)
        driver_profile = DriverProfileForm(
            request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid() and driver_profile.is_valid():
            form.save()
            driver_profile.save(commit=False)
            instance.groups.add(Group.objects.get(
                name=settings.DRIVER_GROUP_NAME))
            driver_profile.save()
            messages.success(request, 'Profile successfully updated')
            return redirect(drive)
        else:
            messages.error(
                request, 'Error while activating driver,,, try again')
    else:
        form = DriverForm(instance=request.user)
        driver_profile = DriverProfileForm(instance=request.user.profile)

    return render(request, 'profiles/profile.html', {'form': form, 'driver_profile': driver_profile})
