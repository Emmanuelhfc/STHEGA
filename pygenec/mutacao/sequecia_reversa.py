from numpy.random import randint
from numpy import array
from pygenec.mutacao.mutacao import Mutacao


class SequenciaReversa(Mutacao):

    def __init__(self, pmut):

        super().__init__(pmut)

    def mutacao(self):
        """
        Alteração genética de membros da população usando sequência reversa.
        """
        nmut = self.selecao()
        if nmut.size != 0:
            for k in nmut:
                i = randint(0, self.ngen)
                j = randint(0, self.ngen)
                while i == j:
                    j = randint(0, self.ngen)
                if i > j:
                    i, j = j, i
                self.populacao[k, i:j] = self.populacao[k, i:j][::-1]
