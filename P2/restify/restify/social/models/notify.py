from django.db import models
from accounts.models.user_model import ThisUser


class Notify(models.Model):
    # the user who is notified
    user = models.ForeignKey(ThisUser, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    # whether the user has read the notification
    is_read = models.BooleanField(default=False)
