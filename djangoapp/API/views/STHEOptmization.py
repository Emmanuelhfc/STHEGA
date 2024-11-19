from API.serializers import*
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser
from drf_spectacular.utils import extend_schema
import logging
from pymoo.core.mixed import MixedVariableGA
from pymoo.optimize import minimize
from API.modules.STHEOptimization.problems import*

logger = logging.getLogger('API')
class STHEOptmizationViewSet(viewsets.ViewSet):
    parser_classes = [MultiPartParser, JSONParser, FormParser,]
    serializer_class = OptimizationInputsSerializer
    

    def sthe_optimization(self, request):
        serializer = OptimizationInputsSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)

        input_id = serializer.validated_data.get('inputs_shell_and_tube')

        problem = STHEProblemGA(input_id)
        algorithm = MixedVariableGA(pop_size=5)

        res = minimize(problem,
               algorithm,
               termination=('n_evals', 100),
               seed=1,
               verbose=True)

        return Response({'msg': f"BEST: F {res.F} - res X= {res.X}"})




