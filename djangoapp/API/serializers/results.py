from rest_framework import serializers
from API.models import Results
from pymoo.core.mixed import MixedVariableGA

class ResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Results
        fields = '__all__'

    
    
    
