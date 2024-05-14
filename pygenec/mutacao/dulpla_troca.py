from numpy.random import randint
from numpy import array
from pygenec.mutacao.mutacao import Mutacao


class DuplaTroca(Mutacao):

    def __init__(self, pmut):

        super().__init__(pmut)
    
    def mutacao(self):
        """Alteração genética de membros da população usando dupla troca."""
        nmut = self.selecao()
        gen1 = array([randint(0, self.ngen)])
        gen2 = array([randint(0, self.ngen)])
        self.populacao[nmut, gen1], self.populacao[nmut, gen2] = self.populacao[nmut, gen2], self.populacao[nmut, gen1]
