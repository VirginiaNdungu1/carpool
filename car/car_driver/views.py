from django.shortcuts import render, redirect
from car import settings
from django.db import transaction
from django.contrib import messages
from .models import DriverProfile
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import DriverForm, DriverProfileForm, TravelPlanForm
from django.contrib.auth.models import User, Group
# Create your views here.


def is_driver(user):
    return user.groups.filter(name='drivers').exists()


@login_required(login_url='/accounts/login/')
@user_passes_test(is_driver)
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

#
# def is_driver(request):
#     user = request.user
#     return user.groups.filter(name='drivers').exists()


@login_required(login_url='/accounts/login')
@user_passes_test(is_driver)
def create_travelplan(request):
    current_user = request.user
    if request.method == 'POST':
        form = TravelPlanForm(request.POST,)
        if current_user.is_authenticated and form.is_valid():
            travel_plan = form.save(commit=False)
            travel_plan.user = current_user
            travel_plan.save()
            return redirect(index)
        else:
            form = TravelPlanForm()
    return render(request, 'travel_plan.html', {"form": form})


@login_required(login_url='/accounts/login')
@user_passes_test(is_driver)
def travelplan_history(request, user_id):
    user = request.user
    travelplans = TravelPlan.objects.get(user_id=user.id)
    return render('travel_history.html', {"travelplans": travelplans})


@login_required(login_url='/accounts/login')
@user_passes_test(is_driver)
def update_travelplan(request, id):
    create_travelplan = False
    user = request.user
    driver_id = user.id
    travel_plan = TravelPlan.objects.get(id=id)
    if request.method == 'POST':
        form = TravelPlanForm(request.POST, obj=TravelPlan)
        if user.is_authenticated and form.is_valid():
            travel_plan.name = form.cleaned_data['name']
            travel_plan.roads = form.cleaned_data['roads']
            travel_plan.depart = form.cleaned_data['depart']
            travel_plan.alight = form.cleaned_data['alight']
            travel_plan.current_location = form.cleaned_data['current_location']
            travel_plan.capacity = form.cleaned_data['capacity']
            travel_plan.created_at = datetime.now()
            travel_plan.user_id = driver_id
            travel_plan.save()
            messages.success(request, 'Profile successfully updated')
            return redirect(travelplan_history, driver_id)
        else:
            messages.error(request, 'Error while updating ,,, try again')
    else:
        form = TravelPlanForm()
    return render(request, 'update_travelplan.html', {"form": form})
