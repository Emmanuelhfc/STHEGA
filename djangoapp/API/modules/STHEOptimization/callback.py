from pymoo.core.callback import Callback
import logging


logger = logging.getLogger('API')
class MyCallback(Callback):
    def __init__(self, isNSGA2=False):
        super().__init__()
        self.isNSGA2 = isNSGA2
        self.generation = 0
        self.data = {
            'gen': [],
            'L': [],
            'objective_function_1': [],
            'objective_function_2': [],
            'constraint_ea_min': [],
            'Ds': [],
            'lc': [],
            'ls': [],
            'A_proj': [],
            'A_nec': [],
            'Nt': [],
            'Nb': [],
            'Re_t': [],
            'Res': [],
            'jl': [],
            'js': [],
            'jb': [],
            'jr': [],
            'jc': [],
            'delta_PT': [],
            'delta_Ps': [],
            'hio': [],
            'hs': [],

        }

    def notify(self, algorithm):
        self.generation += 1

        for ind in algorithm.pop.get("X"):
            results = ind['results']
            self.data["gen"].append(self.generation)
            self.data["L"].append(results["L"])
            self.data["objective_function_1"].append(results["objective_function_1"])
            if self.isNSGA2:
                self.data["objective_function_2"].append(results["objective_function_2"])
            self.data["constraint_ea_min"].append(results["constraint_ea_min"])
            self.data["Ds"].append(results["Ds"])
            self.data["lc"].append(results["lc"])
            self.data["ls"].append(results["ls"])
            self.data["A_proj"].append(results["A_proj"])
            self.data["A_nec"].append(results["A_nec"])
            self.data["Nt"].append(results["Nt"])
            self.data["Nb"].append(results["Nb"])
            self.data["Re_t"].append(results["Re_t"])
            self.data["Res"].append(results["Res"])
            self.data["jl"].append(results["jl"])
            self.data["js"].append(results["js"])
            self.data["jb"].append(results["jb"])
            self.data["jr"].append(results["jr"])
            self.data["jc"].append(results["jc"])
            self.data["delta_PT"].append(results["delta_PT"])
            self.data["delta_Ps"].append(results["delta_Ps"])
            self.data["hio"].append(results["hio"])
            self.data["hs"].append(results["hs"])