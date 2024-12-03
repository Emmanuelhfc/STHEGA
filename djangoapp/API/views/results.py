from API.serializers import*
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser
from drf_spectacular.utils import extend_schema
from API.models import Results
import logging

logger = logging.getLogger('API')
class ResultsViewSet(viewsets.ModelViewSet):
    queryset = Results.objects.all().order_by('id')
    serializer_class = ResultsSerializer
    parser_classes = [MultiPartParser, JSONParser, FormParser,]



