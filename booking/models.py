from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# class User(AbstractUser):
    # pass

# Vaccination Center model
class VaccinationCenter(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    available_slots = models.IntegerField()

    def __str__(self):
        return self.name
    

# Booking Model

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='bookings')
    center = models.ForeignKey(VaccinationCenter, on_delete=models.CASCADE)
    booking_date = models.DateField()
    is_confirmed = models.BooleanField(default=False)