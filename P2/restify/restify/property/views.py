from django.shortcuts import render
from .models.property import Property
from .serilaizers import PropertySerializer
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class PorpertyCreate(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PropertySerializer