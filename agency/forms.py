from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import Trip

class TripForm (ModelForm):
    class Meta:
        model = Trip
        fields = (
            'from_where_city', 'from_where_airport', 
            'to_where_city', 'to_where_airport',
            'to_where_hotel'
            )
            