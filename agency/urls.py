from django.urls import path

from . import views


app_name = "agency" 

urlpatterns = [
 path("trips/", views.trips, name= "trips"),
 path("add_trip/", views.add_trip, name= "add_trip"),
]
