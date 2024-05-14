from numpy.random import random
from numpy import array, argsort
from pygenec.populacao.populacao import Populacao
from pygenec.selecao.selecao import Selecao


class Classificacao(Selecao):

    def __init__(self, populacao: Populacao) -> None:
        """ Seleciona indivíduos usando o método da Classificacao

        Args:
            populacao (Populacao): _description_
        """
        super().__init__(populacao)

    def selecionar(self, fitness):
        if fitness is None:
            fitness = self.populacao.avalia()
        
        classificacao = argsort(fitness) + 1
        total = classificacao.sum()
        parada = total * random()
        parcial = 0
        i = 0

        for i in range(classificacao.size):
            parcial += classificacao[i]
            if parcial >= parada:
                break
        return i