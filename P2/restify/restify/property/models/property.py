from django.db import models
from accounts.models.user_model import ThisUser

# Create your models here.

# amenities
# class Amenity(models.Model):
#     # these fields are requried
#     name = models.CharField(max_length=100)

# property
class Property(models.Model):
    # these fields are requried
    property_name = models.CharField(max_length=100)
    owner = models.ForeignKey(ThisUser, on_delete=models.CASCADE)
    province = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    num_of_guests = models.IntegerField()
    num_of_beds = models.IntegerField()
    price_per_night = models.IntegerField()
    # amenities = models.ManyToManyField(Amenity, blank=False)
    # these fields are not required
    # picture = models.ImageField(upload_to='property_pics', blank=True)

