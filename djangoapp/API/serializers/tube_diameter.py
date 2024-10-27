from rest_framework import serializers
from API.models import TubeDiameter


class TubeDiameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = TubeDiameter
        fields = '__all__'
    