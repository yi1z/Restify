from django.db import models
from django.contrib.auth.models import User, AbstractUser
from property import models as PropertyModel



# Create your models here.

# user
class ThisUser(models.Model):
    # default user model fields
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # additional fields
    # can be blank
    avatar = models.ImageField(upload_to='avatars', blank=True)
    phone_num = models.CharField(max_length=20, blank=True)
