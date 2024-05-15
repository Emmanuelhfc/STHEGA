from numpy.random import choice, random
from numpy import array
from pygenec.mutacao.mutacao import Mutacao


class MutacaoHibridaBin(Mutacao):

    def __init__(self, pmut, size_genes_bins, list_parans_cromo, dict_categorical_values):
        """ Toda a população pode ser submetida a mutação, testa gene por gene de acordo com pmut, se entrar na
        condição escolhe um valor aleatório

        Args:
            pmut (_type_): _description_
        """
        self.size_genes_bins = size_genes_bins
        self.list_parans_cromo = list_parans_cromo
        self.dict_categorical_values = dict_categorical_values

        super().__init__(pmut)
    
    def mutacao_individual(self, cromossomo):
        
        for i in range(len(cromossomo)):
            sort = random()
            
            if sort <= self.pmut and i < self.size_genes_bins:  #Para os binários
                cromossomo[i] = 1 - int(cromossomo[i])

            elif sort <= self.pmut and i > self.size_genes_bins:
                param = self.list_parans_cromo[i]
                list_values = self.dict_categorical_values[param]
                cromossomo[i] = choice(list_values)
        return cromossomo

    def mutacao(self):
        """Alteração genética de membros da população usando dupla troca."""
        for i, cromo in enumerate(self.populacao):
            print(f'Cromossomo {i}')
            self.populacao[i, :] = self.mutacao_individual(cromo)



