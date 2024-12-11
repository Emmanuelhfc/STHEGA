from rest_framework import serializers
from API.models import File, Charts
from pymoo.core.mixed import MixedVariableGA

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'

class ChartsSerializer(serializers.ModelSerializer):
    files = FileSerializer(many=True)
    class Meta:
        model = Charts
        fields = '__all__'

    
    
    
