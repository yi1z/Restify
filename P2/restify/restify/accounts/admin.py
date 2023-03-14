from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ThisUser, Reserve
from .serializers import ThisUserSerializer

# Register your models here.
class ThisAdmin(UserAdmin):
    model = ThisUser
    list_display = ['username', 'email', 'phone_num', 'first_name', 'last_name', 'avatar']

admin.site.register(ThisUser, ThisAdmin)
admin.site.register(Reserve)