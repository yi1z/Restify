from django.db import models
from property import models as PropertyModel
from .user_model import ThisUser


# if a user has a property
class HasProperty(models.Model):
    user = models.ForeignKey(ThisUser, on_delete=models.CASCADE)
    property = models.ForeignKey(PropertyModel.Property, on_delete=models.CASCADE)