from django.urls import path

from . import views


app_name = "agency" 

urlpatterns = [
 path("trips/", views.trips, name= "trips")
]
