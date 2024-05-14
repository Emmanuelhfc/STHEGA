from numpy.random import randint, random
from numpy import array
from pygenec.cruzamento.cruzamento import Cruzamento, NoCompatibleIndividualSize
from random import sample

class KPontos(Cruzamento):


    def __init__(self, tamanho_populacao):
        super().__init__(tamanho_populacao)

    def cruzamento(self, progenitor1, progenitor2):
        """
        Cruzamento de dois indivíduos via k pontos.
        
        Entrada:
            progenitor1 - Primeiro indivíduo
            progenitor2 - Segundo indivíduo
            
        O tamanho de ambos os indivíduos deve ser igual, do contrário um erro será levantado.
        """
        n1 = len(progenitor1)
        n2 = len(progenitor2)
        
        if n1 != n2:
            msg = "Tamanho ind1 {0} diferente de ind2 {1}".format(n1, n2)
            raise NoCompatibleIndividualSize(msg)
        

        kp = randint(1, n1)

        points = sample(range(1, n1), kp)
        points.sort()

        # print("kp", kp)
        # print("points", points)

        child1 = progenitor1.copy()
        child2 = progenitor2.copy()

        for i, point in enumerate(points):
            if (i % 2) != 0:
                child1[last_point:point] = progenitor2[last_point:point]
                child2[last_point:point] = progenitor1[last_point:point]
            last_point = point

        i+=1

        if (i % 2) != 0:
            child1[last_point:] = progenitor2[last_point:]
            child2[last_point:] = progenitor1[last_point:]

        return child1, child2
