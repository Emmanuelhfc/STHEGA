
from API.modules.STHEOptimization.problems import STHEProblem
from API.models import InputsShellAndTube, Results
from API.modules.CascoTubo import CascoTubo, TubeCountError
from API.serializers import ResultsSerializer

import logging

logger = logging.getLogger('API')

class STHEProblemNSGAII(STHEProblem):
    def __init__(self, inputs_shell_and_tube_id, **kwargs):
        super().__init__(inputs_shell_and_tube_id=inputs_shell_and_tube_id, n_ieq_constr=1, n_obj=2, **kwargs)

    def STHE_calculte(self, input:InputsShellAndTube):
        try:
            shell_and_tube = self.default_calculate_sthe(input)
            results_args = shell_and_tube.results()
            objective_function_1 = shell_and_tube.A_proj
            objective_function_2 = shell_and_tube.objective_function_perda_carga_total()
            constraint_ea_max = shell_and_tube.restricao_EA_max()
            constraint_ea_min = shell_and_tube.restricao_EA_min()
            error = False
        
        except TubeCountError:
            logger.warning('Erro na contagem de tubos')
            results_args = {}
            objective_function_1 = 10**6
            objective_function_2 = 10**6
            constraint_ea_max = 10**6
            constraint_ea_min = 10**6
            error = True

        result = Results(
            inputs = input,
            calculation_id = self.calculation_id,
            objective_function_1 = objective_function_1,
            objective_function_2 = objective_function_2,
            constraint_ea_max = constraint_ea_max,
            constraint_ea_min = constraint_ea_min,
            error = error,
            **results_args
        )

        if self.save:
            result.save()

        return ResultsSerializer(result).data

    def _evaluate(self, X, out, *args, **kwargs):
        sthe = self.set_shte_inputs(X)
        sthe_calculate = self.STHE_calculte(sthe)
        f1 = sthe_calculate['objective_function_1']
        f2 = sthe_calculate['objective_function_2']
        g1 = sthe_calculate['constraint_ea_min']

        
        X['results_id'] = sthe_calculate['id']
        out["F"] = [f1, f2]
        out['G'] = g1
