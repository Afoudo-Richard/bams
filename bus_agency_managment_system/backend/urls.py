from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
    path('drivers/', views.drivers, name='drivers'),
    path('add_driver/', views.add_driver, name='add_driver'),
    path('update_driver/<str:pk>', views.update_driver, name='update_driver'),
    path('delete_driver/<str:pk>', views.delete_driver, name='delete_driver'),
    path('buses/', views.buses, name='buses'),
    path('update_bus/<str:pk>', views.update_driver, name='update_bus'),
    path('delete_delete/<str:pk>', views.delete_driver, name='delete_bus'),
    path('bookings/', views.bookings, name='bookings'),
    path('available_trips/', views.available_trips, name='available_trips'),
    path('trip_details/<str:id>/', views.trip_details, name='trip_details'),
    path('trips/', views.trips, name='trips'),
    path('users/', views.users, name='users'),
    path('parcels/', views.parcels, name='parcels'),
    path('book/', views.book, name='book'),
    path('user_parcels/<str:id>', views.user_parcels, name='user_parcels'),
    path('make_user_admin/', views.make_user_admin, name='make_user_admin'),
    path('change_active_status/', views.change_active_status, name='change_active_status'),
    path('send_sms/', views.send_sms, name='send_sms'),
    path('change_book_status/', views.change_book_status, name='change_book_status'),
    path('user_bookings/', views.user_bookings, name='user_bookings'),


]