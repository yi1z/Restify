from rest_framework.serializers import ModelSerializer, CharField, IntegerField, DateField, FloatField, DateTimeField
from .models.property import Property
from .models.property_availability import PropertyAvailability
from django.core.exceptions import PermissionDenied, ValidationError

class PropertySerializer(ModelSerializer):
    owner_username = CharField(source='owner.username', read_only=True, allow_null=False)
    property_name = CharField()
    province = CharField()
    address = CharField()
    num_of_guests = IntegerField()
    num_of_beds = IntegerField()

    class Meta:
        model = Property
        fields = ['property_name', 'owner_username', 'province', 'address', 'num_of_guests', 'num_of_beds']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['owner'] = user
        return super().create(validated_data)
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['property_id'] = instance.id
        return representation
    
class PropertyEditSerializer(ModelSerializer):

    class Meta:
        model = Property
        fields = ['property_name', 'province', 'address', 'num_of_guests', 'num_of_beds']

    def update(self, instance, validated_data):
        instance.property_name = validated_data.get('property_name', instance.property_name)
        instance.province = validated_data.get('province', instance.province)
        instance.address = validated_data.get('address', instance.address)
        instance.num_of_guests = validated_data.get('num_of_guests', instance.num_of_guests)
        instance.num_of_beds = validated_data.get('num_of_beds', instance.num_of_beds)
        instance.save()
        return instance
    
class AvailabilitySerializer(ModelSerializer):
    start_date = DateField()
    end_date = DateField()
    price = FloatField()

    class Meta:
        model = PropertyAvailability
        fields = ['start_date', 'end_date', 'price']

    def create(self, validated_data):
        user = self.context['request'].user
        property_id = self.context['view'].kwargs['property_id']
        try:
            property = Property.objects.get(id=property_id)
        except Property.DoesNotExist:
            raise PermissionDenied("Property does not exist.")
        if property.owner != user:
            raise PermissionDenied("You are not the owner of this property.")
        validated_data['property'] = property
        return super().create(validated_data)

class AvailabilityEditSerializer(ModelSerializer):

    class Meta:
        model = PropertyAvailability
        fields = ['start_date', 'end_date', 'price']

    def update(self, instance, validated_data):
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance