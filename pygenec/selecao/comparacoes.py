from numpy.random import random
from numpy import array 
import matplotlib.pyplot as plt

def selecionar_roleta(fitness):
        fmin = fitness.min()

        # Normaliza para que todos valores sejam > 0
        if fmin <= 0:
            fitness = fitness - fmin + 1
        total = fitness.sum()
        parada = total *random()
        parcial = 0

        for i in range(fitness.size):
            parcial += fitness[i]
            if parcial >= parada:
                break
        return i
def comparacao_roleta():
    fitness = array([5, 10, 15, 16, 17])

    porcents = array([0  for _ in range(fitness.size)])
    range_value  = 10000
    for ind in range(range_value):
        val = selecionar_roleta(fitness) 

        porcents[val] = porcents[val] + 1

    porcents = porcents/range_value


    labels = [str(x) for x in fitness]
    quantidades = porcents

    # Criar o gráfico de pizza
    fig = plt.figure(figsize=(100, 100))

    real = fig.add_subplot(121)
    real.pie(quantidades, labels=labels, autopct='%1.1f%%', startangle=140)
    teorico = fig.add_subplot(122)
    percents_teorico = fitness/fitness.sum()
    teorico.pie(percents_teorico, labels=labels, autopct='%1.1f%%', startangle=140)
    # teorico = "Probabilidade teórica"


    # Mostrar o gráfico

    plt.show()

comparacao_roleta()




