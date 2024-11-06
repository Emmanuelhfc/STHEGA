from rest_framework import serializers
from API.models import InputsShellAndTube
from pymoo.core.mixed import MixedVariableGA




class InputsShellAndTubeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InputsShellAndTube
        fields = '__all__'

    
    
    
