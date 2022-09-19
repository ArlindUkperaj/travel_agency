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


class City(models.Model):
    name = models.CharField(max_length=80)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    
    class Meta:
        db_table = "cities"
    
    def __str__(self):
        return self.name
    

class Hotel(models.Model):
    name = models.CharField(max_length=80)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    stars = models.CharField(max_length=7)
    description = models.TextField
    
    class Meta:
        db_table = "hotels"
    
    def __str__(self):
        return self.name


class Airport(models.Model):
    name = models.CharField(max_length=80)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    
    
    class Meta:
        db_table = "airport"
    
    def __str__(self):
        return self.name
    
# class ArrivingAirport(models.Model):
#     name = models.CharField(max_length=80)
#     city = models.ForeignKey(City, on_delete=models.CASCADE)
    
    
#     class Meta:
#         db_table = "arriving_airport"
    
#     def __str__(self):
#         return self.name
    
class Trip(models.Model):

    # trip_type = [
    #     ("BB", "BB - Bed & Breakfast"),
    #     ("HB", "HB - Half Board"),
    #     ("FB", "FB - Full Board"),
    #     ("AI", "AI - All Inclusive")
    # ]
      
    from_where_city = models.ForeignKey(City, on_delete= models.CASCADE, related_name="city from where +")
    from_where_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="airport from where +")
    to_where_city = models.ForeignKey(City, on_delete= models.CASCADE, related_name="city to where +")
    to_where_airport = models.ForeignKey(Airport, on_delete= models.CASCADE, related_name="airport to where +")
    to_where_hotel = models.ForeignKey(Hotel, on_delete= models.CASCADE, related_name="hotel to where +")
    # date_of_departure = models.DateField
    # date_of_return = models.DateField
    # # number_of_days = days
    # # type: (BB - bed & breakfast, HB – half board, FB – full board, AI – all inclusive )
    # # price_for_adult = ?
    # # price_for_child = ?
    # # promoted = ?
    # # number_of_places_adults = ?
    # # number_of_places_children = ?
    
    class Meta:
        db_table = "trips"

    
    def __str__(self):
        return f"{self.from_where_city}--{self.to_where_city}"
    
    
    # def days(date_of_departure, date_of_return):
    #     if date_of_return:
    #         return date_of_departure - date_of_return
    #     else:
    #         return 'please selecet return date'


  
