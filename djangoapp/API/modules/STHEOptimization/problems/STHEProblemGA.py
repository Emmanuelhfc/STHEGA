
from API.modules.STHEOptimization.problems import STHEProblem
from API.models import InputsShellAndTube, Results
from API.modules.CascoTubo import CascoTubo, TubeCountError
from API.serializers import ResultsSerializer

import logging

logger = logging.getLogger('API')

class STHEProblemGA(STHEProblem):
    def __init__(self, inputs_shell_and_tube_id, save=False, fator_area_proj=1, n_ieq_constr=1, **kwargs):
        super().__init__(inputs_shell_and_tube_id, save, fator_area_proj, n_ieq_constr, **kwargs)

    def STHE_calculte(self, input:InputsShellAndTube):
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
            objective_function_1 = shell_and_tube.objective_function_GA(fator_area_proj=self.fator_area_proj)
            constraint_ea_max = shell_and_tube.restricao_EA_max()
            constraint_ea_min = shell_and_tube.restricao_EA_min()
            error = False
        
        except TubeCountError:
            logger.warning('Erro na contagem de tubos')
            results_args = {}
            objective_function_1 = 10**6
            constraint_ea_max = 10**6
            constraint_ea_min = 10**6
            error = True

        result = Results(
            inputs = input,
            calculation_id = self.calculation_id,
            objective_function_1 = objective_function_1,
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
        f = sthe_calculate['objective_function_1']
        g1 = sthe_calculate['constraint_ea_min']

        logger.debug(f)
        
        X['results_id'] = sthe_calculate['id']
        out["F"] = f
        out['G'] = g1

        