from django.db import models


class Continent(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "continents"
    
    
class Country(models.Model):
    name = models.CharField(max_length=80)
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "countries"
    
    def __str__(self):
        return self.name
