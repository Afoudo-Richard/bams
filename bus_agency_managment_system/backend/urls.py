from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('drivers/', views.drivers, name='drivers'),
    path('add_driver/', views.add_driver, name='add_driver'),
    path('update_driver/<str:pk>', views.update_driver, name='update_driver'),
    path('delete_driver/<str:pk>', views.delete_driver, name='delete_driver'),
    path('buses/', views.buses, name='buses'),
    path('update_bus/<str:pk>', views.update_driver, name='update_bus'),
    path('delete_delete/<str:pk>', views.delete_driver, name='delete_bus'),
    path('bookings/', views.bookings, name='bookings'),
    path('trips/', views.trips, name='trips'),
    path('parcels/', views.parcels, name='parcels'),

]