from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import ThisUser
from django.contrib.auth.models import User

class ThisUserSerializer(ModelSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    phone_number = serializers.CharField()
    email = serializers.EmailField()
    password1 = serializers.CharField()
    password2 = serializers.CharField()

    class Meta:
        model = ThisUser
        fields = ['password', 'first_name', 'last_name', 'email', 'phone_number']
    

    # We want to generate a new User and save to the databse.
    def create(self, validated_data):
        # Testing purpose:
        print(validated_data)
        User

        return super().create(validated_data)
    
    # We may need the update function later:
    def upadate(self, instance, validate_data):
        # TODO
        pass