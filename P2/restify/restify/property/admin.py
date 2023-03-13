from django.contrib import admin
from .models.property import Property
from .models.property_availability import PropertyAvailability

# Register your models here.
admin.site.register(Property)
admin.site.register(PropertyAvailability)