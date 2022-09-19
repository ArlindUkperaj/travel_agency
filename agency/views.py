from django.shortcuts import  render, redirect
from django.urls import reverse
from django.contrib import messages
from .models import Trip

def trips(request):
    trip_list = Trip.objects.all()
    return render(request, "agency/trips.html",
    {'trip_list': trip_list})

