
from API.modules.STHEOptimization.problems import STHEProblem


class STHEProblemGA(STHEProblem):
    def _evaluate(self, X, out, *args, **kwargs):
        try:
            sthe = self.set_shte_inputs(X)
            sthe_calculate = self.STHE_calculte(sthe)
            f = sthe_calculate.objective_GA_EA_and_pressure_drop()
        except:
            f = 1000

        out["F"] = f
        