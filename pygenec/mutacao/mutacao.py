
from numpy.random import random, randint
from numpy import array


class Mutacao:

    def __init__(self, pmut):
        """
        Classe base para operadores de mutação.

        Entrada:
            pmut - probabilidade de ocorrer uma mutação.
        """
        self.pmut = pmut   
        self._populacao = None
        self.npop = None
        self.ngen = None

    def _set_populacao(self, populacao):
        self._populacao = populacao
        self.npop = populacao.shape[0]
        self.ngen = populacao.shape[1]
    
    def _get_populcao(self):
        return self._populacao

    populacao = property(_get_populcao, _set_populacao)