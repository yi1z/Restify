from django.db import models
from accounts.models.user_model import ThisUser
from .property import Property

# property availability
class PropertyAvailability(models.Model):
    # these fields are requried
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    price = models.FloatField(blank=True)
    # these fields are not required
    # price = models.FloatField(blank=False)