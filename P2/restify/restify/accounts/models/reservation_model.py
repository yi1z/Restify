from django.db import models
from property.models import Property
from .user_model import ThisUser


# reservation
class Reserve(models.Model):
    user = models.ForeignKey(ThisUser, on_delete=models.CASCADE, blank=True)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, blank=True)
    status = models.CharField(max_length=20, blank=True)
    request_date = models.DateTimeField(null=True)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)