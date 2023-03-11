from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import ThisUser
from django.contrib.auth.models import User

class ThisUserSerializer(ModelSerializer):
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    phone_number = serializers.CharField()
    email = serializers.EmailField()
    password1 = serializers.CharField()
    password2 = serializers.CharField()

    class Meta:
        model = ThisUser
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'phone_number', 'avatar']

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("Passwords don't match")
        return data
    
    # We want to generate a new User and save to the databse.
    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'], password=validated_data['password1'],
                                   first_name=validated_data['first_name'], last_name=validated_data['last_name'],
                                   email=validated_data['email'])
        final_user = ThisUser.objects.create(user=user,
                                             phone_number=validated_data['phone_number'],
                                             avatar=validated_data['avatar'])
        return final_user
    
    # We may need the update function later:
    def upadate(self, instance, validate_data):
        instance.username = validate_data.get('username', instance.username)
        instance.first_name = validate_data.get('first_name', instance.first_name)
        instance.last_name = validate_data.get('last_name', instance.last_name)
        instance.phone_number = validate_data.get('phone_number', instance.phone_number)
        instance.email = validate_data.get('email', instance.email)
        instance.avatar = validate_data.get('avatar', instance.avatar)
        instance.save()
        return instance