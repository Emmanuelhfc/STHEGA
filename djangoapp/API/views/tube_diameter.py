from API.serializers import*
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser
from drf_spectacular.utils import extend_schema
from API.models import TubeDiameter
import logging

logger = logging.getLogger('API')
class TubeDiameterViewSet(viewsets.ModelViewSet):
    queryset = TubeDiameter.objects.all().order_by('id')
    serializer_class = TubeDiameterSerializer
    parser_classes = [MultiPartParser, JSONParser, FormParser,]



