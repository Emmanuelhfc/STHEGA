from API.serializers import*
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser
from django.http import FileResponse, Http404
from drf_spectacular.utils import extend_schema
from API.models import InputsShellAndTube
import logging

logger = logging.getLogger('API')
class InputsShellAndTubeViewSet(viewsets.ModelViewSet):
    queryset = InputsShellAndTube.objects.all().order_by('id')
    serializer_class = InputsShellAndTubeSerializer
    parser_classes = [MultiPartParser, JSONParser, FormParser,]


    @extend_schema(
            request=InputsShellAndTubeSerializer
    )
    def shell_and_tube_avaliation(self, request):
        
        serializer = InputsShellAndTubeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        logger.debug(serializer.validated_data)

