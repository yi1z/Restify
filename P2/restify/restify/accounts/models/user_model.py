from django.db import models
from django.contrib.auth.models import User, AbstractUser
from property import models as PropertyModel



# Create your models here.

# user
class ThisUser(AbstractUser):
    phone_num = models.CharField(max_length=20, blank=True)
    avatar = models.ImageField(upload_to='avatar', blank=True, null=True)
    password1 = models.CharField(max_length=20, blank=True, null=True)
    password2 = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.username
