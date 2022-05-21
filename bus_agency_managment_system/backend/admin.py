from django.contrib import admin

# Register your models here.

from .models import *
#admin.site.register(User)
admin.site.register(Driver)
admin.site.register(Bus)
admin.site.register(TravelSchedule)
admin.site.register(Booking)
admin.site.register(Parcel)
admin.site.register(AccountCategory)




