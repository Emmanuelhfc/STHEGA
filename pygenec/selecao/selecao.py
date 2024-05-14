from numpy import array
from pygenec.populacao.populacao import Populacao

class Selecao:

    def __init__(self, populacao: Populacao ) -> None:
        """Selecionar indivíduos para cruzamento

        Args:
            populacao (array): Objeto criado a partir da classe	Populacao
        """

        self.populacao = populacao

    def selecionar(self, fitness):
        """ Por padrão não implementado, retorna os
        ídices dos indivíduos selecionados.

        Args:
            fitness (_type_): _description_

        Raises:
            NotImplementedError: _description_
        """


        raise NotImplementedError("A ser implementado")
    
    def selecao(self, n: int, fitness:array = None) -> array:
        """_summary_

        Args:
            n (int): tamanho da subpopulação de selecionados
            fitness (array, optional): array de avaliação da população
        
        Return
            array: array de inivíduos selecionados    
        """

        progenitores = array([self.selecionar(fitness) for _ in range(n)])

        return self.populacao.populacao[progenitores]
        



if __name__ == "__main__":
    a = Selecao(array([0,1]))

    a.selecionar(10)