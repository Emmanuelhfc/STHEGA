
from pygenec.populacao.populacao import Populacao
from pygenec.selecao.selecao import Selecao
from numpy.random import choice
from random import randint
from numpy import  where


class Torneio(Selecao):

    def __init__(self, populacao: Populacao, tamanho = 10) -> None:
        """ Selecão de indivíduos da populçao por torneio

        Args:
            populacao (Populacao): _description_
        """
        super().__init__(populacao)
        self.tamanho = tamanho

    def selecionar(self, fitness: list):
        if fitness is None:
            fitness = self.populacao.avalia()

        tamanho = self.tamanho

        subgrupo = choice(fitness, size= tamanho)
        campeao = subgrupo.max()

        i = where(fitness == campeao)[0][0]

        return i