from numpy.random import randint
from numpy import argsort, unique
from pygenec.populacao.populacao import Populacao


class PopulacaoDefault(Populacao):

    def __init__(self, avaliacao, genes_totais, tamanho_populacao):
        super().__init__(avaliacao, genes_totais, tamanho_populacao)

    def gerar_populacao(self):
        # size -> (nº de arrays, tamanho do array)
        self.populacao = randint(0, 2,
                                 size=(self.tamanho_populacao, self.genes_totais),
                                 dtype='b'
                                 )
        
    
    
    