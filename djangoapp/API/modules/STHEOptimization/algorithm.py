import math
from copy import deepcopy

import numpy as np

from pymoo.algorithms.base.genetic import GeneticAlgorithm
from pymoo.algorithms.soo.nonconvex.ga import FitnessSurvival
from pymoo.core.duplicate import ElementwiseDuplicateElimination
from pymoo.core.individual import Individual
from pymoo.core.infill import InfillCriterion
from pymoo.core.population import Population
from pymoo.core.problem import Problem
from pymoo.core.sampling import Sampling
from pymoo.core.variable import Choice, Real, Integer, Binary, BoundedVariable
from pymoo.operators.crossover.sbx import SBX, SimulatedBinaryCrossover
from pymoo.operators.crossover.ux import UX, UniformCrossover
from pymoo.operators.mutation.bitflip import BFM
from pymoo.operators.mutation.pm import PM
from pymoo.operators.mutation.rm import ChoiceRandomMutation
from pymoo.operators.repair.rounding import RoundingRepair
from pymoo.operators.selection.rnd import RandomSelection
from pymoo.operators.selection.tournament import TournamentSelection
from pymoo.operators.selection.tournament import compare, TournamentSelection
from pymoo.util.display.single import SingleObjectiveOutput
from pymoo.algorithms.moo.nsga2 import RankAndCrowding
from pymoo.util.dominator import Dominator
import logging
import random



logger = logging.getLogger('API')

def custom_binary_tournament(pop, P, algorithm, **kwargs):
    n_tournaments, n_parents = P.shape

    if n_parents != 2:
        raise ValueError("Only implemented for binary tournament!")

    S = np.full(n_tournaments, np.nan)

    for i in range(n_tournaments):

        a, b = P[i, 0], P[i, 1]
        a_cv, a_f, b_cv, b_f = pop[a].CV[0], pop[a].F, pop[b].CV[0], pop[b].F
        rank_a, cd_a = pop[a].get("rank", "crowding")
        rank_b, cd_b = pop[b].get("rank", "crowding")

        logger.debug(f'a_f={a_f}')
        logger.debug(f'b_f={b_f}')
        logger.debug(f'cd_a={cd_a}')
        logger.debug(f'cd_b={cd_b}')

        # if at least one solution is infeasible
        if a_cv > 0.0 or b_cv > 0.0:
            S[i] = compare(a, a_cv, b, b_cv, method='smaller_is_better', return_random_if_equal=True)

        # both solutions are feasible
        else:
            rel = Dominator.get_relation(a_f, b_f)
            if rel == 1:
                S[i] = a
            elif rel == -1:
                S[i] = b

            # if rank or domination relation didn't make a decision compare by crowding
            # if np.isnan(S[i]):
            #     S[i] = compare(a, cd_a, b, cd_b, method='larger_is_better', return_random_if_equal=True)

            if np.isnan(S[i]):
                # Sorteia entre a e b
                S[i] = random.choice([a, b])

    return S[:, None].astype(int, copy=False)


def binary_tournament_mono(pop, P, **kwargs):
    # The P input defines the tournaments and competitors
    n_tournaments, n_competitors = P.shape

    if n_competitors != 2:
        raise Exception("Only pressure=2 allowed for binary tournament!")

    # the result this function returns
    import numpy as np
    S = np.full(n_tournaments, -1, dtype=int)

    # now do all the tournaments
    for i in range(n_tournaments):
        a, b = P[i]
        
        if pop[a].F < pop[b].F:
            S[i] = a
        else:
            S[i] = b

    return S
class CustomMixedVariableMating(InfillCriterion):

    def __init__(self,
                 selection=TournamentSelection(func_comp=binary_tournament_mono),
                 crossover=None,
                 mutation=None,
                 repair=None,
                 eliminate_duplicates=True,
                 n_max_iterations=100,
                 **kwargs):

        super().__init__(repair, eliminate_duplicates, n_max_iterations, **kwargs)

        if crossover is None:
            crossover = {
                Binary: UX(),
                Real: SBX(prob=1),
                Integer: SBX(vtype=float, repair=RoundingRepair()),
                Choice: UX(prob=1),
            }

        if mutation is None:
            mutation = {
                Binary: BFM(),
                Real: PM(),
                Integer: PM(vtype=float, repair=RoundingRepair()),
                Choice: ChoiceRandomMutation(),
            }

        self.selection = selection
        self.crossover = crossover
        self.mutation = mutation

    def _do(self, problem, pop, n_offsprings, parents=False, **kwargs):

        # So far we assume all crossover need the same amount of parents and create the same number of offsprings
        XOVER_N_PARENTS = 2
        XOVER_N_OFFSPRINGS = 2

        # the variables with the concrete information
        vars = problem.vars

        # group all the variables by their types
        vars_by_type = {}
        for k, v in vars.items():
            clazz = type(v)

            if clazz not in vars_by_type:
                vars_by_type[clazz] = []
            vars_by_type[clazz].append(k)

        # # all different recombinations (the choices need to be split because of data types)
        recomb = []
        for clazz, list_of_vars in vars_by_type.items():
            if clazz == Choice:
                for e in list_of_vars:
                    recomb.append((clazz, [e]))
            else:
                recomb.append((clazz, list_of_vars))

        # create an empty population that will be set in each iteration
        off = Population.new(X=[{} for _ in range(n_offsprings)])

        if not parents:
            n_select = math.ceil(n_offsprings / XOVER_N_OFFSPRINGS)
            pop = self.selection(problem, pop, n_select, XOVER_N_PARENTS, **kwargs)

        for clazz, list_of_vars in recomb:

            crossover = self.crossover[clazz]
            assert crossover.n_parents == XOVER_N_PARENTS and crossover.n_offsprings == XOVER_N_OFFSPRINGS

            _parents = [
                [Individual(X=np.array([parent.X[var] for var in list_of_vars], dtype="O" if clazz is Choice else None)) 
                  for parent in parents] 
                for parents in pop
            ]

            _vars = {e: vars[e] for e in list_of_vars}
            _xl = np.array([vars[e].lb if hasattr(vars[e], "lb") else None for e in list_of_vars])
            _xu = np.array([vars[e].ub if hasattr(vars[e], "ub") else None for e in list_of_vars])
            _problem = Problem(vars=_vars, xl=_xl, xu=_xu)

            _off = crossover(_problem, _parents, **kwargs)

            mutation = self.mutation[clazz]
            _off = mutation(_problem, _off, **kwargs)

            for k in range(n_offsprings):
                for i, name in enumerate(list_of_vars):
                    off[k].X[name] = _off[k].X[i]

        return off


class MixedVariableSampling(Sampling):

    def _do(self, problem, n_samples, **kwargs):
        V = {name: var.sample(n_samples) for name, var in problem.vars.items()}

        X = []
        for k in range(n_samples):
            X.append({name: V[name][k] for name in problem.vars.keys()})

        return X


class MixedVariableDuplicateElimination(ElementwiseDuplicateElimination):

    def is_equal(self, a, b):
        a, b = a.X, b.X
        for k, v in a.items():
            if k not in b or b[k] != v:
                return False
        return True


def groups_of_vars(vars):
    ret = {}
    for name, var in vars.items():
        if var.__class__ not in ret:
            ret[var.__class__] = []

        ret[var.__class__].append((name, var))

    return ret


class CustomMixedVariableGA(GeneticAlgorithm):
    def __init__(self,
                 pop_size=50,
                 n_offsprings=None,
                 output=SingleObjectiveOutput(),
                 sampling=MixedVariableSampling(),
                 mating=CustomMixedVariableMating(eliminate_duplicates=MixedVariableDuplicateElimination(), selection=TournamentSelection(func_comp=binary_tournament_mono)),
                 eliminate_duplicates=MixedVariableDuplicateElimination(),
                 survival=FitnessSurvival(),
                 **kwargs):
        super().__init__(pop_size=pop_size, n_offsprings=n_offsprings, sampling=sampling, mating=mating,
                         eliminate_duplicates=eliminate_duplicates, output=output, survival=survival, **kwargs)
        

class CustomMixedVariableNSGAII(GeneticAlgorithm):
    def __init__(self,
                 pop_size=50,
                 n_offsprings=None,
                 output=SingleObjectiveOutput(),
                 sampling=MixedVariableSampling(),
                 mating=CustomMixedVariableMating(eliminate_duplicates=MixedVariableDuplicateElimination(), selection=TournamentSelection(func_comp=custom_binary_tournament)),
                 eliminate_duplicates=MixedVariableDuplicateElimination(),
                 survival=RankAndCrowding(),
                 **kwargs):
        super().__init__(pop_size=pop_size, n_offsprings=n_offsprings, sampling=sampling, mating=mating,
                         eliminate_duplicates=eliminate_duplicates, output=output, survival=survival, **kwargs)
