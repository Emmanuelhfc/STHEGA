from API.serializers import*
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser
from drf_spectacular.utils import extend_schema
from API.models import Results
from API.pagination import*
from django_filters.rest_framework import DjangoFilterBackend
import logging

logger = logging.getLogger('API')
@extend_schema(tags=['RESULTS'])
class ResultsViewSet(viewsets.ModelViewSet):
    queryset = Results.objects.all().order_by('id')
    serializer_class = ResultsSerializer
    parser_classes = [MultiPartParser, JSONParser, FormParser,]
    pagination_class = GenericPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('id', 'calculation_id',)



