from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import ThisUser, Reserve
from django.contrib.auth.models import User
from collections import OrderedDict


class ThisUserSerializer(ModelSerializer):
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    phone_num = serializers.CharField()
    email = serializers.EmailField()
    password1 = serializers.CharField()
    password2 = serializers.CharField()
    avatar = serializers.ImageField()

    class Meta:
        model = ThisUser
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'phone_num', 'avatar']

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("Passwords don't match")

        username = data['username']
        if ThisUser.objects.filter(username=username).exists():
            raise serializers.ValidationError("Username already exists")
        
        # edit the password
        data['password'] = data['password1']
        data['password1'] = None
        data['password2'] = None
        # if data['avatar'] is None:
        #     data['avatar'] = '../default_user.png'
        return data
    
    # We want to generate a new User and save to the databse.
    def create(self, validated_data):
        user = ThisUser.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    # hide certain fields from the response
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        return OrderedDict([
            ('username', ret['username']),
            ('first_name', ret['first_name']),
            ('last_name', ret['last_name']),
            ('phone_num', ret['phone_num']),
            ('email', ret['email']),
            ('avatar', ret['avatar']),
        ])
    
    
    # We may need the update function later:
class ThisUserUpdateSerializer(ModelSerializer):
    username = serializers.CharField(max_length=None, min_length=None, allow_blank=True, trim_whitespace=True,required=False)
    first_name = serializers.CharField(max_length=None, min_length=None, allow_blank=True, trim_whitespace=True,required=False)
    last_name = serializers.CharField(max_length=None, min_length=None, allow_blank=True, trim_whitespace=True,required=False)
    phone_num = serializers.CharField(max_length=None, min_length=None, allow_blank=True, trim_whitespace=True,required=False)
    email = serializers.EmailField(max_length=None, min_length=None, allow_blank=True,required=False)
    password1 = serializers.CharField(max_length=None, min_length=None, allow_blank=True, trim_whitespace=True, required=False)
    password2 = serializers.CharField(max_length=None, min_length=None, allow_blank=True, trim_whitespace=True, required=False)
    avatar = serializers.ImageField(max_length=None, allow_empty_file=True, required=False)
    class Meta:
        model = ThisUser
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'phone_num', 'avatar']

    def validate(self, data):
    
        if ('password1' in data and 'password2' in data) and data['password1'] != data['password2']:
            raise serializers.ValidationError({'password2': "Passwords don't match"})
        fields = ['username', 'first_name', 'last_name', 'phone_num', 'email', 'avatar']
        for field in fields:
            if field in data and not data[field]:
                data.pop(field) 
        return data

    def upadate(self, instance, validate_data):
        instance.username = validate_data.get('username', instance.username)
        instance.first_name = validate_data.get('first_name', instance.first_name)
        instance.last_name = validate_data.get('last_name', instance.last_name)
        instance.phone_num = validate_data.get('phone_num', instance.phone_num)
        instance.email = validate_data.get('email', instance.email)
        instance.avatar = validate_data.get('avatar', instance.avatar)
        if validate_data['password1'] != None:
            instance.set_password(validate_data['password1'])
        instance.save()
        return instance
    
class ListReservationSerializer(ModelSerializer):

    class Meta:
        model = Reserve
        fields = ['user', 'property', 'reservation_date', 'request_date', 'status', 'reservation_customer']

    

    