from django.contrib import admin
from .models import User,VaccinationCenter,Booking
# Register your models here.

# admin.site.register(User)
admin.site.register(VaccinationCenter)
admin.site.register(Booking)
