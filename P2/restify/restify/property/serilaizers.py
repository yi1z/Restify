from rest_framework.serializers import ModelSerializer, CharField
from .models.property import Property
from .models.property_availability import PropertyAvailability

class PropertySerializer(ModelSerializer):
    owner_username = CharField(source='owner.username', read_only=True, allow_null=False)

    class Meta:
        model = Property
        fields = ['property_name', 'owner_username', 'province', 'address', 'num_of_guests', 'num_of_beds', 'price_per_night']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['owner'] = user
        return super().create(validated_data)
    
class PropertyEditSerializer(ModelSerializer):
    property_name = CharField(max_length=None, min_length=None, allow_blank=True, trim_whitespace=True,required=False)
    province = CharField(max_length=None, min_length=None, allow_blank=True, trim_whitespace=True,required=False)
    address = CharField(max_length=None, min_length=None, allow_blank=True, trim_whitespace=True,required=False)
    num_of_guests = CharField(max_length=None, min_length=None, allow_blank=True, trim_whitespace=True,required=False)
    num_of_beds = CharField(max_length=None, min_length=None, allow_blank=True, trim_whitespace=True,required=False)
    price_per_night = CharField(max_length=None, min_length=None, allow_blank=True, trim_whitespace=True,required=False)

    class Meta:
        model = Property
        fields = ['property_name', 'province', 'address', 'num_of_guests', 'num_of_beds', 'price_per_night']

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.province = validated_data.get('province', instance.province)
        instance.address = validated_data.get('address', instance.address)
        instance.num_of_guests = validated_data.get('num_of_guests', instance.num_of_guests)
        instance.num_of_beds = validated_data.get('num_of_beds', instance.num_of_beds)
        instance.price_per_night = validated_data.get('price_per_night', instance.price_per_night)
        instance.save()
        return instance
    
class AvailabilitySerializer(ModelSerializer):
    class Meta:
        model = PropertyAvailability
        fields = ['start_date', 'end_date']

    def create(self, validated_data):
        property_id = self.context['request'].parser_context['kwargs']['property_id']
        property = Property.objects.get(id=property_id)
        validated_data['property'] = property
        return super().create(validated_data)