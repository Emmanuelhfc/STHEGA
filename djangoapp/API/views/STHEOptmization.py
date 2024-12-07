from API.serializers import*
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser
from pymoo.termination.default import DefaultSingleObjectiveTermination
from drf_spectacular.utils import extend_schema
import logging
from pymoo.core.mixed import MixedVariableGA
from pymoo.optimize import minimize
from API.modules.STHEOptimization.problems import*
from API.modules.STHEOptimization.callback import MyCallback




logger = logging.getLogger('API')

class STHEOptmizationViewSet(viewsets.ViewSet):
    parser_classes = [MultiPartParser, JSONParser, FormParser,]
    serializer_class = GAInputsSerializer
    
    @extend_schema(
        tags=['GA OPTIMIZATION'],
        responses=ResultsSerializer
    )
    def ga_sthe_optimization(self, request):
        serializer = GAInputsSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)

        input_id = serializer.validated_data.get('inputs_shell_and_tube')
        pop_size = serializer.validated_data.get('pop_size')
        n_max_gen = serializer.validated_data.get('n_max_gen')
        n_max_evals = serializer.validated_data.get('n_max_evals')
        save_results = serializers.validated_data.get('save_results')

        termination = DefaultSingleObjectiveTermination(
            xtol=1e-8,
            cvtol=1e-6,
            ftol=1e-6,
            period=20,
            n_max_gen=n_max_gen,
            n_max_evals=n_max_evals
        )


        problem = STHEProblemGA(input_id)
        algorithm = MixedVariableGA(pop_size=pop_size)

        callback = MyCallback()

        res = minimize(problem,
               algorithm,
               termination= termination,
               seed=1,
               verbose=True,
               callback=callback)
        
       
        results = Results.objects.get(id=res.X['results_id'])

        return Response(ResultsSerializer(results).data)




