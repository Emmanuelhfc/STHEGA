from pygenec.selecao.selecao import Selecao
from pygenec.populacao.populacao import Populacao
from pygenec.cruzamento.cruzamento import Cruzamento
from pygenec.mutacao.mutacao import Mutacao
from random import random

class Evolucao:
    
    def __init__(self, populacao: Populacao, selecao: Selecao, cruzamento: Cruzamento, mutacao: Mutacao):
        """
        Usando operadores genéticos, coloca uma população para evoluir.

        Entrada:
            populacao - Objeto do tipo Populacao
            selecao - Objeto do tipo Selecao
            cruzamento - Objeto do tipo cruzamento
            mutacao - Objeto do tipo Mutacao.
        """
        self.populacao = populacao
        self.selecao = selecao
        self.cruzamento = cruzamento
        self.mutacao = mutacao
        self._geracao = 0
        self._melhor_solucao = None
        self._nsele = None
        self._pcruz = None
        self._epidemia = None
        self._manter_melhor = True
        self._fitness = None
        self._first = True
    
    def _set_epidemia(self, epidemia):
        self._epidemia = epidemia
    
    def _set_manter_melhor(self, manter):
        self._manter_melhor = manter

    def _set_nsele(self, nsele):
        self._nsele = nsele

    def _get_nsele(self):
        return self._nsele

    def _set_pcruz(self, pcruz):
        self._pcruz = pcruz

    def _get_pcruz(self):
        return self._pcruz
    
    def	_get_first(self):
        return self._first
    
    def	_set_first(self, first):
        self._first	= first
    
    def	_get_epidemia(self):
        return self._epidemia

    def	_get_manter_melhor(self):
        return self._manter_melhor
    


    @property
    def melhor_solucao(self):
        return self._melhor_solucao

    @property
    def geracao(self):
        return self._geracao

    def evoluir(self):
        """
        Evolução elitista, por uma geração, da população.
        """
        if self._first is True:
            self._fitness = self.populacao.avalia()
            self._first = False
        self._melhor_solucao = self.populacao.populacao[-1].copy()
        subpopulacao = self.selecao.selecao(self._nsele, fitness=self._fitness)
        populacao = self.cruzamento.descendentes(subpopulacao, pcruz=self._pcruz)
        self.mutacao.populacao = populacao
        self.mutacao.mutacao()
        self.populacao.populacao[:] = populacao[:]
        
        if self._manter_melhor is True:
            self.populacao.populacao[0] = self._melhor_solucao

        self._geracao += 1
        if self._epidemia is not None and self._geracao % self._epidemia == 0 and random() < 0.8:
            print('Epidemia na geração ', self._geracao)
            self.populacao.gerar_populacao()
            self.populacao.populacao[0] = self._melhor_solucao


        
        self._fitness = self.populacao.avalia()
        return self._fitness.min(), self._fitness.max()

    nsele = property(_get_nsele, _set_nsele)
    pcruz = property(_get_pcruz, _set_pcruz)
    first =	property(_get_first, _set_first)
    epidemia = property(_get_epidemia, _set_epidemia)
    manter_melhor = property(_get_manter_melhor, _set_manter_melhor)

