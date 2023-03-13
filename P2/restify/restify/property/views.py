from django.shortcuts import render
from .models.property import Property
from .serilaizers import PropertySerializer, AvailabilitySerializer
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
    serializer_class = PropertySerializer

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

    def perform_create(self, serializer):
        property_id = self.kwargs['property_id']
        user = self.request.user
        property = Property.objects.get(id=property_id)
        if property.owner != user:
            raise PermissionDenied("You are not the owner of this property.")
        serializer.save(property=property)
