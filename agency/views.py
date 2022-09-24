from django.shortcuts import  render, redirect
from django.http import HttpResponseRedirect
# from django.urls import reverse
# from django.contrib import messages

from .models import Trip
from .forms import TripForm


def trips(request):
    trip_list = Trip.objects.all()
    return render(request, "agency/trips.html",
    {'trip_list': trip_list})


def add_trip(request):
        submitted = False
        if request.method == "POST":
            form = TripForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/add_trip?submitted=True')
            
        else:
            form = TripForm
            if 'submitted' in request.GET:
                submitted = True
        return render(request, "agency/add_trip.html", {'form':form, 'submitted':submitted})