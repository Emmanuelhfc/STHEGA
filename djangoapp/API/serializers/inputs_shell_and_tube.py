from rest_framework import serializers
from API.models import InputsShellAndTube


class InputsShellAndTubeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = InputsShellAndTube
        fields = '__all__'
    
    
