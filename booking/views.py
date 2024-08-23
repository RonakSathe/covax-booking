from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest
from .models import VaccinationCenter, Booking
from .forms import BookingForm

# User Registration
def register(request: HttpRequest):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# User Login
def login(request: HttpRequest):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('centers')
    return render(request, 'login.html')

# User Logout
def logout(request: HttpRequest):
    auth_logout(request)
    return redirect('login')

# List Centers
def centers(request: HttpRequest):
    centers = VaccinationCenter.objects.all()
    return render(request, 'centers.html', {'centers': centers})

# Book a Slot
def book(request: HttpRequest):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            if booking.center.available_slots > 0:
                booking.save()
                booking.center.available_slots -= 1
                booking.center.save()
                return redirect('centers')
            else:
                return render(request, 'book.html', {'form': form, 'error': 'No slots available'})
    else:
        form = BookingForm()
    return render(request, 'book.html', {'form': form})
