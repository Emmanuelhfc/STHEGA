from API.serializers import*
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser
from drf_spectacular.utils import extend_schema
from API.models import Charts
from django_filters.rest_framework import DjangoFilterBackend
import logging

logger = logging.getLogger('API')

@extend_schema(tags=['CHARTS'])
class ChartViewSet(viewsets.ModelViewSet):
    queryset = Charts.objects.all().order_by('id')
    serializer_class = ChartsSerializer
    parser_classes = [MultiPartParser, JSONParser, FormParser,]
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('id', 'calculation_id',)


