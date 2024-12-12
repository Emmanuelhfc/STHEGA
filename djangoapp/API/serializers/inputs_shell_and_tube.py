from rest_framework import serializers
from API.models import InputsShellAndTube, Pitch, TubeDiameter, TubeInternDiameter
from pymoo.core.mixed import MixedVariableGA



class TubeInternDiameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = TubeInternDiameter
        fields = '__all__'

class TubeDiameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = TubeDiameter
        fields = '__all__'
class PitchSerializer(serializers.ModelSerializer):
    de = TubeDiameterSerializer()
    class Meta:
        model = Pitch
        fields = '__all__'

class InputsShellAndTubeSerializer(serializers.ModelSerializer):
    pitch = PitchSerializer()
    di = TubeInternDiameterSerializer()
    class Meta:
        model = InputsShellAndTube
        fields = '__all__'

    
    
    
