from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.contrib import messages
from .forms import *
from .models import *
from .decorators import *

# Create your views here.
@unauthenticated_user
def index(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, "Username or Password is incorrect")
        

    context = {
        
    }
    return render(request, 'backend/login.html')

@unauthenticated_user    
def register(request):
    
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "successfully created user " + user)
            return redirect('login')

    context = {
        'form': form
    }
    return render(request, 'backend/register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required()
def dashboard(request):
    users = User.objects.all()
    drivers = Driver.objects.all()
    buses = Bus.objects.all()
    parcels_in_transit = Parcel.objects.filter(parcel_status = "In Transit")
    parcels_recieved = Parcel.objects.filter(parcel_status = "Recieved")
    parcels_arrived = Parcel.objects.filter(parcel_status = "Arrived")
    parcels_delivered = Parcel.objects.filter(parcel_status = "Delivered")




    context = {
        'total_users': users.count(),
        'total_drivers': drivers.count(),
        'total_buses': buses.count(),
        'total_parcels_in_transit': parcels_in_transit.count(),
        'total_parcels_recieved': parcels_recieved.count(),
        'total_parcels_delivered': parcels_delivered.count(),
        'total_parcels_arrived': parcels_arrived.count(),
    }
    return render(request, 'backend/index.html', context)

@login_required()
def drivers(request):
    drivers = Driver.objects.all()
    context = {
        'drivers': drivers
    }
    return render(request, 'backend/drivers.html', context)


@login_required()
def add_driver(request):
    context = {
        'title': "Add Driver"
    }
    if request.method == "POST":
        form = DriverForm(request.POST)
        if form.is_valid():
            print(request.POST)
            form.save()
            return redirect('/drivers')
    return render(request, 'backend/form/driver_form.html', context)

@login_required()
def update_driver(request, pk):
    driver = Driver.objects.get(id=pk)
    form = DriverForm(instance=driver)
    context = {'form':form, 'title':"Edit Driver"}
    if request.method == "POST":
        form = DriverForm(request.POST, instance=driver)
        if form.is_valid():
            print(request.POST)
            form.save()
            return redirect('/drivers')
    return render(request, 'backend/form/driver_form.html', context)

@login_required()
def delete_driver(request, pk):
    driver = Driver.objects.get(id=pk)
    driver.delete()
    return redirect('/drivers')

def buses(request):
    buses = Bus.objects.all()
    context = {
        'buses': buses
    }
    return render(request, 'backend/buses.html', context)

def bookings(request):
    bookings = Booking.objects.all()
    context = {
        'bookings': bookings
    }
    return render(request, 'backend/bookings.html', context)

def trips(request):
    trips = Trip.objects.all()
    context = {
        'trips': trips
    }
    return render(request, 'backend/trips.html', context)

def parcels(request):
    bookings = Parcel.objects.all()
    context = {
        'parcels': parcels
    }
    return render(request, 'backend/parcels.html', context)