from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from . serializers import ThisUserSerializer
from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# Create your views here.

class UserCreate(CreateAPIView):
    serializer_class = ThisUserSerializer

class UserEdit(UpdateAPIView):
    serializer_class = ThisUserSerializer
    permission_classes = (IsAuthenticated,)

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
