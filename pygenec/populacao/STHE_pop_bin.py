from numpy.random import randint, choice
from numpy import argsort, unique, array, concatenate
from pygenec.populacao.populacao import Populacao



class PopSTHEBin(Populacao):

    def __init__(self, avaliacao, size_genes_bins, pop_size, dict_categorical_values: dict, dict_index_caracterisc: dict):
        """_summary_

        Args:
            avaliacao (_type_): _description_
            genes_totais (_type_): _description_
            tamanho_populacao_binarios (_type_): _description_
            dict_categorical_values (dict): _description_
                Ex:
                    self.dict_categorical_values = {
                        'Ds': lista com valores ["Dc"],
                        'n': lista com valores['n'],
                        'de_inch': lista com valores['de_inch'],
                        'layout': lista com valores['layout'],
                        'pitch_inch': lista com valores['pitch_inch']
                    } 
            dict_index_caracterisc (dict): dicionário que traduz os cromossomos para caracterisitca. Informa o índice de onde começa e onde termina.
            Não é preciso passar no dicionário os valores categóricos
                Ex:
                    dict_index_caracterisc = {
                        'Ds': [10,10],
                        'L': [0, 10]
                    }
        """

        self.dict_index_caracterisc = dict_index_caracterisc
        self.dict_categorical_values = dict_categorical_values
        self.size_genes_bins = size_genes_bins

        
        i = size_genes_bins
        for value in self.dict_categorical_values:
            index = [i, i+1]
            self.dict_index_caracterisc[value] = index
            i += 1


        list_parans_cromo = []
        for param in self.dict_index_caracterisc:
            start, end = self.dict_index_caracterisc[param]
            list_ = [param for i in range(start, end)]
            list_parans_cromo.extend(list_)
        
        self.list_parans_cromo = list_parans_cromo
        print(list_parans_cromo)


        genes_totais = size_genes_bins + len(self.dict_categorical_values)

        super().__init__(avaliacao, genes_totais, pop_size)

    def gerar_populacao(self):

        population = randint(0, 2, size=(self.tamanho_populacao, self.size_genes_bins), dtype='b')

        categorical_pop = {}
        for param in self.dict_categorical_values:
            list_values = self.dict_categorical_values[param]
            ramdom_choice = choice(list_values, self.tamanho_populacao)
            
            categorical_pop = array([array([choice]) for choice in ramdom_choice])
            
            population = concatenate((population, categorical_pop), axis=1)
        
        print(population)
        self.populacao = population

if __name__ == '__main__':
    ...
    # def avalicao():
    #     return


    # dic_categorical_values ={
    #     'param_1': ['banana', 'peira', 'maça', 'abacaxi'],
    #     'param_2': ['peixe', 'bife', 'camarão']
    # }

    # dict_index_carac = {
    #     'param3': [0, 5],
    #     'param4': [5, 10]
    # }

    # size_gen_bins = 10
    # a = PopSTHEBin(avalicao, size_gen_bins, 20,dic_categorical_values,dict_index_carac)
    # a.gerar_populacao()

    # list_params_cromo = a.list_parans_cromo
    # dict_categorical_values = a.dict_categorical_values

    # m = MutacaoHibridaBin(0.05, size_gen_bins, list_params_cromo, dict_categorical_values)
    # m.populacao = a.populacao
    # m.mutacao()
    # print(m.populacao)
