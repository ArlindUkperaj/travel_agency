from tkinter import CASCADE
from django.db import models

class Continent(models.Model):
    name_of_continent = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name_of_continent
    
    
class Country(models.Model):
    name_of_country = models.CharField(max_length=80)
    name_of_continent = models.ForeignKey(Continent, on_delete=models.CASCADE)
    
    
