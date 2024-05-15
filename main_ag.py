from numpy import exp, array
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from numpy import mgrid
from matplotlib.animation import FuncAnimation
from pygenec.selecao import*
from pygenec.cruzamento import*
from pygenec.mutacao import*
from pygenec.populacao.STHE_pop_bin import PopSTHEBin
from pygenec.evolucao import Evolucao


# def func(x, y):
#     tmp = 3 * exp(-(y + 1) ** 2 - x ** 2) * (x - 1) ** 2 \
#         - (exp(-(x + 1) ** 2 - y ** 2) / 3) \
#         + exp(-x ** 2 - y ** 2) * (10 * x ** 3 - 2 * x + 10 * y ** 5)
#     return tmp

# def bin(matrix):
#     """ Converte a matrix de bin para int

#     Args:
#         matrix (_type_): _description_

#     Returns:
#         _type_: _description_
#     """
#     coluns_number = matrix.shape[1]
#     line_number = matrix.shape[0]
#     cnt = array([2 ** i for i in range(coluns_number)]) #   vetor com potências para 2. 2^0 2^1 2^2 ...

#     return array([(cnt * matrix[i, :]).sum() for i in range(line_number)])

# def xy(populacao):
#     colunas = populacao.shape[1]
#     meio = colunas // 2
#     maiorbin = 2.0 ** meio - 1.0
#     # Intervalo de busca
#     nmin = -3
#     nmax = 3
#     #Constante de normalização
#     const = (nmax - nmin) / maiorbin

#     # Garante que valores estejam dentro do intervalo, normalização
#     x = nmin + const * bin(populacao[:, :meio])
#     y = nmin + const * bin(populacao[:, meio:])
#     return x, y

# def avaliacao(populacao):
#     """Retorna um vetor com a aaliação da população, cada item corresponde a avaliação
#     de um indivíduo da população.

#     Args:
#         populacao (_type_): _description_

#     Returns:
#         _type_: _description_
#     """
#     x, y = xy(populacao)
#     tmp = -func(x, y)
#     return tmp



# genes_totais = 32
# tamanho_populacao = 50
# populacao = Populacao(avaliacao, genes_totais, tamanho_populacao)
# populacao.gerar_populacao()
# print("===========", len(populacao.populacao))

# selecao = Torneio(populacao)
# cruzamento = KPontos(tamanho_populacao)
# mutacao = Flip(0.9)

# evolucao = Evolucao(populacao, selecao, cruzamento, mutacao)

# evolucao.nsele = 10
# evolucao.pcruz = 0.5
# evolucao.epidemia = 17

# fig = plt.figure(figsize=(100, 100))
# ax = fig.add_subplot(111, projection="3d")
# X, Y = mgrid[-3:3:30j, -3:3:30j]
# Z = func(X, Y)
# ax.plot_wireframe(X, Y, Z)

# x, y = xy(populacao.populacao)
# z = func(x, y)
# graph = ax.scatter(x, y, z, s=50, c='red', marker='D')

# num_geracoes = 100

# def update(frame):
#     print(frame)
#     min_fit, max_fit = evolucao.evoluir()
#     x, y = xy(populacao.populacao)
#     z = func(x, y)
#     graph._offsets3d = (x, y, z)
#     if frame == (num_geracoes -1):
#         print('Indíviduo dessa geração com maior fitness: ', populacao.populacao[-1])
#         x_max, y_max = xy(array([populacao.populacao[-1]]))
#         print('X_max: ', x_max)
#         print('Y_min: ', y_max)
#         print('Valor máximo: ', max_fit)

#         print('Valor min: ', min_fit)


# ani = FuncAnimation(fig, update, frames= range(num_geracoes), repeat=False)
# plt.show()


def avalicao():
    return


dic_categorical_values ={
    'param_1': ['banana', 'peira', 'maça', 'abacaxi'],
    'param_2': ['peixe', 'bife', 'camarão']
}

dict_index_carac = {
    'param3': [0, 5],
    'param4': [5, 10]
}

size_gen_bins = 10
a = PopSTHEBin(avalicao, size_gen_bins, 20,dic_categorical_values,dict_index_carac)
a.gerar_populacao()

list_params_cromo = a.list_parans_cromo
dict_categorical_values = a.dict_categorical_values
print('----------------------------------------------------')
m = MutacaoHibridaBin(0.05, size_gen_bins, list_params_cromo, dict_categorical_values)
m.populacao = a.populacao
m.mutacao()
print(m.populacao)
