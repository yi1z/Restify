from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from . serializers import ThisUserSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class UserCreate(CreateAPIView):
    serializer_class = ThisUserSerializer

class UserEdit(CreateAPIView):
    serializer_class = ThisUserSerializer
    permission_classes = [IsAuthenticated]
    def get_serializer_context(self):
        return {"request": self.request}
