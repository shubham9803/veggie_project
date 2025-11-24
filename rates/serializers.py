from rest_framework import serializers
from .models import Rate

class RateSerializer(serializers.ModelSerializer):
    added_by = serializers.ReadOnlyField(source='added_by.username')
    verified_by = serializers.ReadOnlyField(source='verified_by.username')

    class Meta:
        model = Rate
        fields = [
            'id', 'vegetable', 'market', 'quantity', 'price',
            'added_by', 'verified_by', 'is_verified', 'created_at'
        ]
