from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from . serializers import ThisUserSerializer
from rest_framework.generics import CreateAPIView

# Create your views here.

class UserCreate(CreateAPIView):
    serializer_class = ThisUserSerializer