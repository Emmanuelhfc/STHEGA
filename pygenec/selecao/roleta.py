from numpy.random import random
from numpy import array
from pygenec.populacao.populacao import Populacao
from pygenec.selecao.selecao import Selecao


class Roleta(Selecao):

    def __init__(self, populacao: Populacao) -> None:
        """ Seleciona indivíduos usando o método da roleta

        Args:
            populacao (Populacao): _description_
        """
        super().__init__(populacao)

    def selecionar(self, fitness):
        
        if fitness is None:
            fitness = self.populacao.avalia()
        fmin = fitness.min()

        # Normaliza para que todos valores sejam > 0
        if fmin <= 0:
            fitness = fitness - fmin + 1
        total = fitness.sum()
        parada = total * random()
        parcial = 0
        i = 0

        for i in range(fitness.size):
            parcial += fitness[i]
            if parcial >= parada:
                break
        return i