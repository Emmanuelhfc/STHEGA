
from API.modules.STHEOptimization.problems import STHEProblem

import logging

logger = logging.getLogger('API')

class STHEProblemGA(STHEProblem):
    def _evaluate(self, X, out, *args, **kwargs):
        sthe = self.set_shte_inputs(X)
        sthe_calculate = self.STHE_calculte(sthe)
        f = sthe_calculate['objective_function_1']

        X['results_id'] = sthe_calculate['id']
        out["F"] = f
        