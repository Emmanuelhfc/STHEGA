from API.serializers import*
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser
from drf_spectacular.utils import extend_schema
import logging

logger = logging.getLogger('API')
class STHEOptmizationViewSet(viewsets.ViewSet):
    parser_classes = [MultiPartParser, JSONParser, FormParser,]
    serializer_class = OptimizationInputsSerializer
    

    def sthe_optimization_nsga2(self, request):
        ...



