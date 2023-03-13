from rest_framework.serializers import ModelSerializer, CharField
from .models.property import Property

class PropertySerializer(ModelSerializer):
    owner_username = CharField(source='owner.username', read_only=True, allow_null=False)

    class Meta:
        model = Property
        fields = ['name', 'owner_username', 'province', 'address', 'num_of_guests']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['owner'] = user
        return super().create(validated_data)