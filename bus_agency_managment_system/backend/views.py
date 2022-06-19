
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User, Group

from twilio.rest import Client


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
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='customer')

            user.groups.add(group)
            messages.success(request, "successfully created user " + username)
            return redirect('login')

    context = {
        'form': form
    }
    return render(request, 'backend/register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required()
@admin_only
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
@allowed_users(allowed_roles=['customer'])
def user_dashboard(request):

    user = User.objects.get(id=request.user.id)
    user_parcels = user.parcel_set.all()
    user_bookings = user.booking_set.all()

    context = {
       'total_user_parcels': user_parcels.count(),
       'total_user_bookings': user_bookings.count(), 
    }
    return render(request, 'backend/user_dashboard.html', context)

@login_required()
@allowed_users(allowed_roles=['admin'])
def drivers(request):
    drivers = Driver.objects.all()
    context = {
        'drivers': drivers
    }
    return render(request, 'backend/drivers.html', context)


@login_required()
@allowed_users(allowed_roles=['admin'])
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
@allowed_users(allowed_roles=['admin'])
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
@allowed_users(allowed_roles=['admin'])
def delete_driver(request, pk):
    driver = Driver.objects.get(id=pk)
    driver.delete()
    return redirect('/drivers')

@login_required()
@allowed_users(allowed_roles=['admin'])
def buses(request):
    buses = Bus.objects.all()
    context = {
        'buses': buses
    }
    return render(request, 'backend/buses.html', context)

@login_required()
@allowed_users(allowed_roles=['admin'])
def bookings(request):
    bookings = Booking.objects.all()
    context = {
        'bookings': bookings
    }
    return render(request, 'backend/bookings.html', context)

@login_required()
@allowed_users(allowed_roles=['customer'])
def available_trips(request):
    trips = Trip.objects.all()
    context = {
        'trips': trips
    }
    return render(request, 'backend/available_trips.html', context)

@login_required()
@allowed_users(allowed_roles=['customer'])
def book(request):
    if request.method == "POST":
        # create booking
        trip = Trip.objects.get(id=request.POST.get('trip_id'))
        user = User.objects.get(id=request.user.id)
        booking = Booking.objects.create(trip = trip, user = user, booking_status='Pending')
        return redirect('user_bookings')
    trips = Trip.objects.all()
    context = {
        'trips': trips
    }
    return render(request, 'backend/available_trips.html', context)


@login_required()
@allowed_users(allowed_roles=['customer'])
def trip_details(request, id):
    trip = Trip.objects.get(id=id)
    context = {
        'trip': trip
    }
    return render(request, 'backend/trip_details.html', context)

@login_required()
@allowed_users(allowed_roles=['admin'])
def trips(request):
    trips = Trip.objects.all()
    context = {
        'trips': trips
    }
    
    return render(request, 'backend/trips.html', context)

@login_required()
@allowed_users(allowed_roles=['admin'])
def parcels(request):
    bookings = Parcel.objects.all()
    context = {
        'parcels': parcels
    }
    return render(request, 'backend/parcels.html', context)

@login_required()
@allowed_users(allowed_roles=['customer'])
def user_parcels(request, id):
    user = User.objects.get(id=id)
    user_parcels = user.parcel_set.all()

    context = {
        'bookings': user_parcels
    }
    return render(request, 'backend/user_parcel.html', context)

@login_required()
@allowed_users(allowed_roles=['customer'])
def user_bookings(request):
    user = User.objects.get(id=request.user.id)
    user_bookings = user.booking_set.all()

    context = {
        'bookings': user_bookings
    }
    return render(request, 'backend/user_bookings.html', context)

@login_required()
@allowed_users(allowed_roles=['admin'])
def users(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'backend/users.html', context)

@login_required()
@allowed_users(allowed_roles=['admin'])
def make_user_admin(request):
    user = User.objects.get(id=request.POST.get('id'))
    user.is_staff = 1

    user.save()
    return redirect('users')

@login_required()
@allowed_users(allowed_roles=['admin'])
def change_active_status(request):
    user = User.objects.get(id=request.POST.get('id'))
    if user.is_active == 1:
        user.is_active = 0
    else:
        user.is_active = 1

    user.save()
    return redirect('users')

def send_sms(request):
    # Your Account SID from twilio.com/console
    account_sid = "ACc4551514e3378b478c22007da381a060"
    # Your Auth Token from twilio.com/console
    auth_token  = "bc88a737fc0d73375b0a7d2584a48cab"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="+237693386383", 
        from_="+15396666611",
        body="Hello from Python!")

    print(message.sid)
    return HttpResponse("SMS sent")

@login_required()
@allowed_users(allowed_roles=['admin'])
def change_book_status(request):
    if request.method == 'POST':
        booking = Booking.objects.get(id=request.POST.get('id'))
        if request.POST.get('type') == 'approve':

            booking.booking_status = 'Approved'

        elif request.POST.get('type') == 'terminate':
            booking.booking_status = 'Terminated'
        booking.save()
        return redirect('bookings')
    else:
        return HttpResponse("request not valid")
