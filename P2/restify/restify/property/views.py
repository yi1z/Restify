from django.shortcuts import render
from .models.property import Property
from .models.property_availability import PropertyAvailability
from .serilaizers import PropertySerializer, AvailabilitySerializer, PropertyEditSerializer, AvailabilityEditSerializer
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import PermissionDenied
from rest_framework.response import Response


# Create your views here.

class PorpertyCreate(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PropertySerializer

class PorpertyEdit(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PropertyEditSerializer

    def get_object(self):
        property_id = self.kwargs['property_id']
        user = self.request.user
        property = Property.objects.get(id=property_id)
        if property.owner != user:
            raise PermissionDenied("You are not the owner of this property.")
        return property
    
    def get(self, request, *args, **kwargs):
        property = self.get_object()
        serializer = PropertySerializer(instance=property)
        return Response(serializer.data)
    
class PorpertyDelete(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PropertySerializer

    def get_object(self):
        property_id = self.kwargs['property_id']
        user = self.request.user
        property = Property.objects.get(id=property_id)
        if property.owner != user:
            raise PermissionDenied("You are not the owner of this property.")
        return property
    
    def delete(self, request, *args, **kwargs):
        property = Property.objects.get(id=self.kwargs['property_id'])
        property.delete()
        return Response("Property deleted successfully.")
    

class PropertyList(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PropertySerializer

    def get_queryset(self):
        user = self.request.user
        return Property.objects.filter(owner=user)


class AvailabilityCreate(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AvailabilitySerializer


class AvailabilityEdit(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AvailabilityEditSerializer

    def get_object(self):
        avail_id = self.kwargs['avail_id']
        user = self.request.user
        avail = PropertyAvailability.objects.get(id=avail_id)
        if avail.property.owner != user:
            raise PermissionDenied("You are not the owner of this property.")
        return avail
    
    def get(self, request, *args, **kwargs):
        avail = self.get_object()
        serializer = AvailabilitySerializer(instance=avail)
        return Response(serializer.data)
