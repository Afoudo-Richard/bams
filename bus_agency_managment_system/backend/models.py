
import email
from operator import mod
from unicodedata import category, name
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class AccountCategory(models.Model):
    category_name = models.CharField(max_length=200, null=True)
# class User(models.Model):
#     STATUS = (
#         ("Pending", "Pending"),
#         ('Approved', "Approved"),
#         ('Rejected', "Rejected")
#     )
#     account_category = models.ForeignKey(AccountCategory, null=True, on_delete=models.SET_NULL)
#     first_name = models.CharField(max_length=200, null=True)
#     last_name = models.CharField(max_length=200, null=True)
#     phone = models.CharField(max_length=200, null=True)
#     address = models.CharField(max_length=200, null=True)
#     email = models.CharField(max_length=200, null=True)
#     password = models.CharField(max_length=200, null=True)
#     account_status = models.CharField(max_length=200, null=True, choices=STATUS)
#     date_created = models.DateTimeField(auto_now_add=True)
    

#     def __str__(self) -> str:
#         return self.name

class Driver(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone1 = models.CharField(max_length=200, null=True)
    phone2 = models.CharField(max_length=200, null=True, blank=True)

class Bus(models.Model):
    bus_number = models.CharField(max_length=200, null=True)
    bus_plate_number = models.CharField(max_length=200, null=True)
    bus_capacity = models.CharField(max_length=200, null=True)
class TravelSchedule(models.Model):
    
    bus = models.ForeignKey(Bus, on_delete=models.SET_NULL, null=True)
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True)
    starting_point= models.CharField(max_length=200, null=True)
    destination = models.CharField(max_length=200, null=True)
    departure_datetime = models.DateTimeField()
    estimated_arrival_time = models.CharField(max_length=200, null=True)
    travel_fare_amount = models.IntegerField()
    avaible_seats = models.IntegerField(default= 0)

    remarks = models.CharField(max_length=300, null=True, blank=True)

    def bus_capacity(self):
        return self.bus.bus_capacity



class Booking(models.Model):
    STATUS = (
        ("Pending", "Pending"),
        ('Approved', "Approved"),
        ('Rejected', "Rejected"),
    )
    schedule = models.ForeignKey(TravelSchedule, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    date_of_booking = models.DateTimeField(auto_now=True)
    booking_status = models.CharField(max_length=200, null=True, choices=STATUS)

class Parcel(models.Model):
    STATUS = (
        ("Recieved", "Recieved"),
        ('In Transit', "In Transit"),
        ('Arrived', "Arrived"),
        ('Delivered', "Delivered")
    )
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    parcel_description = models.CharField(max_length=200, null=True)
    parcel_starting_point = models.CharField(max_length=200, null=True)
    parcel_destination = models.CharField(max_length=200, null=True)
    parcel_departure_datetime = models.DateTimeField()
    parcel_estimated_arrival_time = models.DateTimeField()
    parcel_fare_amount = models.CharField(max_length=200, null=True)
    parcel_status = models.CharField(max_length=200, null=True, choices=STATUS)
    parcel_remarks = models.CharField(max_length=200, null=True)



    # tags = models.ManyToManyField(Tag)