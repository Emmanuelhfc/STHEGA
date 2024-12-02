from API.serializers import*
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser
from drf_spectacular.utils import extend_schema
import logging
from pymoo.core.mixed import MixedVariableGA
from pymoo.optimize import minimize
from API.modules.STHEOptimization.problems import*
from pymoo.core.callback import Callback

logger = logging.getLogger('API')


class MyCallback(Callback):
    def __init__(self):
        super().__init__()
        self.generation = 0

    def notify(self, algorithm):
        self.generation += 1
        # logger.info(f"Geração: {self.generation}")
        # logger.info("População atual:")
        # for ind in algorithm.pop.get("X"):
        #     logger.info(ind)
class STHEOptmizationViewSet(viewsets.ViewSet):
    parser_classes = [MultiPartParser, JSONParser, FormParser,]
    serializer_class = OptimizationInputsSerializer
    
    
    def sthe_optimization(self, request):
        serializer = OptimizationInputsSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)

        input_id = serializer.validated_data.get('inputs_shell_and_tube')

        problem = STHEProblemGA(input_id)
        algorithm = MixedVariableGA(pop_size=5)

        callback = MyCallback()

        res = minimize(problem,
               algorithm,
               termination=('n_evals', 300),
               seed=1,
               verbose=True,
               callback=callback)

        return Response({'msg': f"BEST: F {res.F} - res X= {res.X}"})




