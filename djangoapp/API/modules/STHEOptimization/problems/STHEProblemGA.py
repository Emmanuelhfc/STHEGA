
from API.modules.STHEOptimization.problems import STHEProblem


class STHEProblemGA(STHEProblem):
    def _evaluate(self, X, out, *args, **kwargs):
        sthe = self.set_shte_inputs(X)
        sthe = self.STHE_calculte(sthe)

        out["F"] = sthe.objective_GA_EA_and_pressure_drop()