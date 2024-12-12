from API.serializers import*
from API.modules.CascoTubo import*
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser
from django.http import FileResponse, Http404
from drf_spectacular.utils import extend_schema
from API.models import InputsShellAndTube, Results
from rest_framework.response import Response
from rest_framework.serializers import Serializer
import logging

logger = logging.getLogger('API')
class STHECalcultionViewSet(viewsets.ViewSet):
    parser_classes = [MultiPartParser, JSONParser, FormParser,]
    serializer_class = Serializer

    @extend_schema(
        tags=['SHELL AND TUBE CALCULATION'],
        responses = ResultsSerializer
    )
    def shell_and_tube_avaliation(self, request, pk):
        input = InputsShellAndTube.objects.get(id=pk)

        shell_and_tube = CascoTubo(input)
        shell_and_tube.filtro_tubos()
        shell_and_tube.area_projeto()
        shell_and_tube.coef_global_min()
        shell_and_tube.conveccao_tubo()
        shell_and_tube.calculos_auxiliares()
        shell_and_tube.trans_cal_casco()
        shell_and_tube.calculo_temp_parede()
        shell_and_tube.coef_global_limpo()
        shell_and_tube.coef_global_sujo()
        shell_and_tube.excesso_area()
        shell_and_tube.perda_carga_tubo()
        shell_and_tube.perda_carga_casco()

        results_args = shell_and_tube.results()

        result = Results.objects.create(
            inputs = input,
            **results_args
        )
        

        return Response(ResultsSerializer(result).data)
        
        

