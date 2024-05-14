from numpy.random import randint
from numpy import argsort, unique


class Populacao():
    
    def __init__(self, avaliacao, genes_totais, tamanho_populacao):
        """Cria e avalia população

        Args:
            avaliacao (function): recebe indivíduos e retorna valor numérico
            genes_totais (_type_): inteiro representando tamanho da cadeia
            tamanho_populacao (_type_): numero total de indivíduos
        """
        self.avaliacao = avaliacao
        self.genes_totais = genes_totais
        self.tamanho_populacao = tamanho_populacao

    def gerar_populacao(self):
        ...

    def avalia(self):
        """ Avalia e ordena uma população de acordo com a avaliação
        """

        u, indices = unique(self.populacao, return_inverse=True, axis=0)
        valores = self.avaliacao(u)
        valores = valores[indices]
        ind = argsort(valores)
        self.populacao[:] = self.populacao[ind]
        
        return valores[ind]
    

if __name__ == "__main__":
    import numpy as np

    a = np.array([
        [0, 0, 1],
        [0, 1, 1]
    ])

    u, indices = unique(a, return_inverse=True, axis=0)

    b = np.array([0, 1, 1, 1, 1])
    print(a[b])