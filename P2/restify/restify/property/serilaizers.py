from rest_framework.serializers import ModelSerializer, CharField
from .models.property import Property
from .models.property_availability import PropertyAvailability

class PropertySerializer(ModelSerializer):
    owner_username = CharField(source='owner.username', read_only=True, allow_null=False)

    class Meta:
        model = Property
        fields = ['property_name', 'owner_username', 'province', 'address', 'num_of_guests']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['owner'] = user
        return super().create(validated_data)
    
class PropertyEditSerializer(ModelSerializer):
    class Meta:
        model = Property
        fields = ['property_name', 'province', 'address', 'num_of_guests']

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.province = validated_data.get('province', instance.province)
        instance.address = validated_data.get('address', instance.address)
        instance.num_of_guests = validated_data.get('num_of_guests', instance.num_of_guests)
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