from django.db import models
from property import models as PropertyModel
from .user_model import ThisUser

# reservation
class Reserve(models.Model):
    user = models.ForeignKey(ThisUser, on_delete=models.CASCADE)
    property = models.ForeignKey(PropertyModel.Property, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    request_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()