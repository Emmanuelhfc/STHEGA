from API.serializers import*
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser
from pymoo.visualization.scatter import Scatter
from pymoo.termination.default import DefaultSingleObjectiveTermination, DefaultMultiObjectiveTermination
from drf_spectacular.utils import extend_schema
import logging
# from pymoo.core.mixed import MixedVariableGA
from API.modules.STHEOptimization.algorithm import CustomMixedVariableGA, CustomMixedVariableNSGAII
from pymoo.optimize import minimize
from API.modules.STHEOptimization.problems import*
from API.modules.STHEOptimization.callback import MyCallback
from API.modules.STHEOptimization.DataProcessor import DataProcessor
import pandas as pd



logger = logging.getLogger('API')

class STHEOptmizationViewSet(viewsets.ViewSet):
    parser_classes = [MultiPartParser, JSONParser, FormParser,]
    serializer_class = GAInputsSerializer
    
    def create_shte_inputs(self, inputs_id, input_data, calculation_id) -> InputsShellAndTube:
        initial_inputs = InputsShellAndTube.objects.get(id=inputs_id).__dict__
        inputs_sthe = InputsShellAndTube(
            T1_hot = initial_inputs["T1_hot"],
            T2_hot = initial_inputs["T2_hot"],
            t1_cold = initial_inputs["t1_cold"],
            t2_cold = initial_inputs["t2_cold"],
            wq = initial_inputs["wq"],
            wf = initial_inputs["wf"],
            cp_quente = initial_inputs["cp_quente"],
            cp_frio = initial_inputs["cp_frio"],
            casco_passagens = initial_inputs["casco_passagens"],
            rho_q = initial_inputs["rho_q"],
            rho_f = initial_inputs["rho_f"],
            mi_q = initial_inputs["mi_q"],
            mi_f = initial_inputs["mi_f"],
            k_q = initial_inputs["k_q"],
            k_f = initial_inputs["k_f"],
            Rd_q = initial_inputs["Rd_q"],
            Rd_f = initial_inputs["Rd_f"],
            tipo_q = initial_inputs["tipo_q"],
            tipo_f = initial_inputs["tipo_f"],
            reference = initial_inputs["reference"],
            perda_carga_admissivel_casco= initial_inputs['perda_carga_admissivel_casco'],
            perda_carga_admissivel_tubo= initial_inputs['perda_carga_admissivel_tubo'],
            calculation_id = calculation_id,

            pressure_class = input_data["pressure_class"],
            shell_thickness_meters = input_data["shell_thickness_meters"],
            lc_percent = input_data["lc_percent"],
            ls_percent = input_data["ls_percent"],
            shell_fluid = input_data["shell_fluid"],
            L = input_data["L_percent"] * input_data["Ds_inch"] * 0.0254,
            Ds_inch = input_data["Ds_inch"],
            n = input_data["n"],
            tube_material= TubeMaterial.objects.get(id=input_data["tube_material_id"]),
            
        )
        pitch = Pitch.objects.get(id= input_data["pitch_id"])
        de = pitch.de

        di = TubeInternDiameter.objects.filter(
            tube_diameter = de.id,
            standard = input_data["di_standard"]
        ).first()
        inputs_sthe.di = di
        inputs_sthe.pitch = pitch

        
        inputs_sthe.save()

        return inputs_sthe
    
    def STHE_save_results(self, input:InputsShellAndTube, calculation_id, isNSGA=False, ) -> Results:
        try:
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
            shell_and_tube.results()
            results_args = shell_and_tube.results()
            if isNSGA:
                objective_function_1 = shell_and_tube.A_proj
                objective_function_2 = shell_and_tube.objective_function_perda_carga_total()
            else:
                objective_function_1 = shell_and_tube.objective_function_GA()
                objective_function_2 = None
            constraint_ea_max = shell_and_tube.restricao_EA_max()
            constraint_ea_min = shell_and_tube.restricao_EA_min()
            error = False
        
        except TubeCountError:
            results_args = {}
            objective_function_1 = 10**6
            if isNSGA:
                objective_function_2 = 10**6
            else:
                objective_function_2 = None
            constraint_ea_max = 10**6
            constraint_ea_min = 10**6
            error = True

        result = Results(
            inputs = input,
            calculation_id = calculation_id,
            objective_function_1 = objective_function_1,
            objective_function_2 = objective_function_2,
            constraint_ea_max = constraint_ea_max,
            constraint_ea_min = constraint_ea_min,
            error = error,
            **results_args
        )

        
        result.save()

        return result

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
        n_max_evals = 10**6
        fator_area_proj = serializer.validated_data.get('fator_area_proj')

        termination = DefaultSingleObjectiveTermination(
            xtol=0,
            cvtol=0,
            ftol=0,
            period=20,
            n_max_gen=n_max_gen,
            n_max_evals=n_max_evals
        )
        problem = STHEProblemGA(input_id, save=False, fator_area_proj=fator_area_proj)
        calculation_id = problem.calculation_id
        algorithm = CustomMixedVariableGA(pop_size=pop_size)
        callback = MyCallback()
        res = minimize(problem,
               algorithm,
               termination= termination,
               seed=1,
               verbose=True,
               callback=callback,
               save_history=True
        )
        
        data_processor = DataProcessor(callback.data, calculation_id, nsga2=False)
        data_processor.process_all_graphs()


        input_data = {
            'shell_thickness_meters': float(res.X['shell_thickness_meters']),
            'ls_percent': float(res.X['ls_percent']),
            'lc_percent': float(res.X['lc_percent']),
            'L_percent': float(res.X['L_percent']),
            'pressure_class': float(res.X['pressure_class']),
            'tube_material_id': int(res.X['tube_material_id']),
            'shell_fluid': str(res.X['shell_fluid']),
            'Ds_inch': float(res.X['Ds_inch']),
            'n': int(res.X['n']),
            'pitch_id': int(res.X['pitch_id']),
            'di_standard': str(res.X['di_standard']),
        }

        inputs_sthe = self.create_shte_inputs(input_id, input_data,calculation_id)
        return Response(ResultsSerializer(self.STHE_save_results(inputs_sthe,calculation_id)).data)

    @extend_schema(
        tags=['NSGAII OPTIMIZATION'],
        request=NSGA2InputsSerializer,
        responses=ResultsSerializer(many=True)
    )
    def nsga2_sthe_optimization(self, request):
        serializer = NSGA2InputsSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)

        input_id = serializer.validated_data.get('inputs_shell_and_tube')
        pop_size = serializer.validated_data.get('pop_size')
        n_max_gen = serializer.validated_data.get('n_max_gen')
        n_max_evals = 10**6
        
        termination = DefaultMultiObjectiveTermination(
            xtol=0,
            cvtol=0,
            ftol=0,
            period=20,
            n_max_gen=n_max_gen,
            n_max_evals=n_max_evals
        )

        problem = STHEProblemNSGAII(input_id)
        calculation_id = problem.calculation_id
        algorithm = CustomMixedVariableNSGAII(pop_size=pop_size)
        callback = MyCallback(isNSGA2=True)

        res = minimize(problem,
               algorithm,
               termination= termination,
               verbose=True,
               callback=callback,
               save_history=True
               )



        # Results
        pareto_front = [inp['ind'] for inp in res.X]
        data_processor = DataProcessor(callback.data, calculation_id, pareto_front_ind=pareto_front)
        data_processor.process_all_graphs()
        
        
        results = []
        for inputs in res.X:

            input_data = {
                'shell_thickness_meters': float(inputs['shell_thickness_meters']),
                'ls_percent': float(inputs['ls_percent']),
                'lc_percent': float(inputs['lc_percent']),
                'L_percent': float(inputs['L_percent']),
                'pressure_class': float(inputs['pressure_class']),
                'tube_material_id': int(inputs['tube_material_id']),
                'shell_fluid': str(inputs['shell_fluid']),
                'Ds_inch': float(inputs['Ds_inch']),
                'n': int(inputs['n']),
                'pitch_id': int(inputs['pitch_id']),
                'di_standard': str(inputs['di_standard']),
            }

            inputs_sthe = self.create_shte_inputs(input_id, input_data,calculation_id)
            results.append(self.STHE_save_results(inputs_sthe,calculation_id,isNSGA=True))
        return Response(ResultsSerializer(results, many=True).data)


