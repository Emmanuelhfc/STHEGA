from API.serializers import*
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
import logging
import pint

logger = logging.getLogger('API')
class UnitConversionViewSet(viewsets.ViewSet):
    parser_classes = [MultiPartParser, ]
    
    @extend_schema(
            request = UnitConversionSerializer
    )
    def conversion(self, request):
        
        data = UnitConversionSerializer(data=request.data)
        data.is_valid(raise_exception=True)

        ureg = pint.UnitRegistry()
        Q_ = ureg.Quantity

        in_base_units = Q_(data.validated_data['input_value'], data.validated_data['input_unit']).to_base_units()
        if data.validated_data['output_unit'] != "si":
            try:
                res = Q_(data.validated_data['input_value'], data.validated_data['input_unit']).to(data.validated_data['output_unit'])
                res = res.magnitude
            except:
                return Response({'msg': 'error'}, status=400)
        else:
            res = in_base_units.magnitude
            data.validated_data['output_unit'] = in_base_units.u.__str__()

        data.validated_data['output_value'] = res

        return Response(data.validated_data)


