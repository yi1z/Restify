from django.db import models
from accounts.models.user_model import ThisUser

# Create your models here.

# property
class Property(models.Model):
    # these fields are requried
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(ThisUser, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    # these fields are not required
    picture = models.ImageField(upload_to='property_pics', blank=True)


# property availability
class PropertyAvailability(models.Model):
    # these fields are requried
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    # these fields are not required
    price = models.FloatField(blank=False)