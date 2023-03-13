from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from . serializers import ThisUserSerializer, ThisUserUpdateSerializer
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import ThisUser

# Create your views here.

class UserCreate(CreateAPIView):
    serializer_class = ThisUserSerializer

class UserEdit(UpdateAPIView):
    serializer_class = ThisUserUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_object_or_404(ThisUser, id=self.kwargs['pk'])
