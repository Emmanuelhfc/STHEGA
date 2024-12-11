from API.serializers import*
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser
from drf_spectacular.utils import extend_schema
from API.models import Results
from API.pagination import*
import logging

logger = logging.getLogger('API')
@extend_schema(tags=['RESULTS'])
class ResultsViewSet(viewsets.ModelViewSet):
    queryset = Results.objects.all().order_by('id')
    serializer_class = ResultsSerializer
    parser_classes = [MultiPartParser, JSONParser, FormParser,]
    pagination_class = GenericPagination



