from django.contrib import admin
from .models import Continent
from .models import Country
from .models import City
from .models import Airport
from .models import Hotel


admin.site.register(Continent)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Airport)
admin.site.register(Hotel)