from django.shortcuts import render, redirect
from car import settings
from django.db import transaction
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RiderForm, RiderProfileForm
from django.contrib.auth.models import User, Group
# Create your views here.


def ride(request):
    return render(request, 'ride.html')


@login_required(login_url='/accounts/login/')
@transaction.atomic
def updateuserprofile(request):
    instance = request.user
    if request.method == 'POST':
        form = RiderForm(request.POST, request.FILES,
                         instance=request.user)
        user_profile = RiderProfileForm(
            request.POST, request.FILES, instance=request.user.rider_profile)
        if form.is_valid() and user_profile.is_valid():
            # instance.groups.add(Group.objects.get(
            #     name=settings.REGISTRATION_DEFAULT_GROUP_NAME))
            form.save()
            user_profile.save(commit=False)
            instance.groups.add(Group.objects.get(
                name=settings.REGISTRATION_DEFAULT_GROUP_NAME))
            messages.success(request, 'Profile successfully updated')
            return redirect(ride)
        else:
            messages.error(
                request, 'Error while updating profile,,, try again')
    else:
        form = RiderForm(instance=request.user)
        user_profile = RiderProfileForm(instance=request.user.rider_profile)

    return render(request, 'profile.html', {'form': form, 'user_profile': user_profile})
