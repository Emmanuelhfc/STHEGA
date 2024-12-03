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

@extend_schema(tags=['INPUTS'])
class InputsShellAndTubeViewSet(viewsets.ModelViewSet):
    queryset = InputsShellAndTube.objects.all().order_by('id')
    serializer_class = InputsShellAndTubeSerializer
    parser_classes = [MultiPartParser, JSONParser, FormParser,]

    # def pop_state_key(self, data:dict):
    #     list_models = [TubeCount, TubeDiameter, Pitch, DeltaSB, Pitch, LiLo, TubeInternDiameter, TubeMaterial, Layout, ConstantsA, ConstantsB, NozzleDiameter]
    #     for item in data:
    #         if type(data[item]) in list_models:
    #             data[item] = data[item].__dict__
    #             data[item].pop('_state')
                
    #     return data

    # @extend_schema(tags=['SHELL AND TUBE CALCULATION'])
    # def shell_and_tube_avaliation(self, request, pk):
    #     input = InputsShellAndTube.objects.get(id=pk)

    #     shell_and_tube = CascoTubo(input)
    #     shell_and_tube.filtro_tubos()
    #     shell_and_tube.area_projeto()
    #     shell_and_tube.coef_global_min()
    #     shell_and_tube.conveccao_tubo()
    #     shell_and_tube.calculos_auxiliares()
    #     shell_and_tube.trans_cal_casco()
    #     shell_and_tube.calculo_temp_parede()
    #     shell_and_tube.coef_global_limpo()
    #     shell_and_tube.coef_global_sujo()
    #     shell_and_tube.excesso_area()
    #     shell_and_tube.perda_carga_tubo()
    #     shell_and_tube.perda_carga_casco()

    #     data = shell_and_tube.__dict__

    #     logger.debug(type(data['de']) == models)

    #     data = self.pop_state_key(data)

    #     # data['de'] = data['de'].__dict__
    #     # data['de'].pop('_state')

    #     # data['pitch'] = data['pitch'].__dict__
    #     # data['pitch'].pop('_state')

    #     # data['layout'] = data['layout'].__dict__
    #     # data['layout'].pop('_state')

    #     # data['di'] = data['di'].__dict__
    #     # data['di'].pop('_state')

    #     # data['tube_material'] = data['tube_material'].__dict__
    #     # data['tube_material'].pop('_state')
        
    #     return Response(data)
        
        

