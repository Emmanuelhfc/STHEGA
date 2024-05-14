from numpy.random import randint
from numpy import array
from pygenec.mutacao.mutacao import Mutacao


class Flip(Mutacao):

    def __init__(self, pmut):

        super().__init__(pmut)
    
    def mutacao(self):
        """Alteração genética de membros da população usando mutação flip."""
        nmut = self.selecao()
        genflip = array([randint(0, self.ngen) for _ in nmut])
        self.populacao[nmut, genflip] = 1 - self.populacao[nmut, genflip]
        