from API.serializers import*
from API.modules.CascoTubo import*
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser
from django.http import FileResponse, Http404
from drf_spectacular.utils import extend_schema
from API.models import InputsShellAndTube, TubeDiameter, Pitch
from rest_framework.response import Response
import logging

logger = logging.getLogger('API')
class InputsShellAndTubeViewSet(viewsets.ModelViewSet):
    queryset = InputsShellAndTube.objects.all().order_by('id')
    serializer_class = InputsShellAndTubeSerializer
    parser_classes = [MultiPartParser, JSONParser, FormParser,]

    @extend_schema(tags=['SHELL AND TUBE CALCULATION'])
    def shell_and_tube_avaliation(self, request, pk):
        input = InputsShellAndTube.objects.get(id=pk)


        shell_and_tube = CascoTubo(input)
        
        data = shell_and_tube.__dict__

        data['de'] = data['de'].__dict__
        data['de'].pop('_state')

        data['pitch'] = data['pitch'].__dict__
        data['pitch'].pop('_state')

        return Response(data)
        
        

