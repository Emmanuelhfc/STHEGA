import pandas as pd
import matplotlib.pyplot as plt
from pymoo.visualization.scatter import Scatter
from io import BytesIO
from django.core.files.base import ContentFile
from API.models import File, Charts
import logging

logger = logging.getLogger('API')
class DataProcessor:
    def __init__(self, data, calcultion_id, nsga2=True, pareto_front_ind=[]):
        self.df = pd.DataFrame(data)
        self.calcultion_id = calcultion_id
        last_gen_number = self.df['gen'].max()
        self.last_gen_data = self.df[self.df['gen'] == last_gen_number]
        self.nsga2 = nsga2
        self.charts = Charts.objects.create(calculation_id = self.calcultion_id)
        if nsga2:
            self.pareto_front = self.df[self.df['ind'].isin(pareto_front_ind)]
            

    def create_and_save_graph(self, x_column, y_column, title, model_field_name) -> File:
        plt.figure(figsize=(8, 6))
        plt.plot(self.df[x_column], self.df[y_column], marker='o', linestyle='-', color='blue')
        plt.title(title)
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.grid(True)
        
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        plt.close()  # Fecha a figura para liberar memória
        
        buffer.seek(0)
        image_file = ContentFile(buffer.read(), name=f"{model_field_name}.png")
        graph = File.objects.create(file=image_file)
        buffer.close()

        return graph
    
    def save_data_as_csv(self):
        buffer = BytesIO()
        self.df.to_csv(buffer, index=False)  
        buffer.seek(0)  
        csv = ContentFile(buffer.read(), name=f"data.csv")
        file = File.objects.create(file=csv)
        buffer.close()
        
        self.charts.csv = file
        self.charts.save()
    
    def pareto_front_chart(self):
        plt.figure(figsize=(8, 6))
        plt.scatter(self.pareto_front['objective_function_1'], self.pareto_front['objective_function_2'], facecolor="none", edgecolor="red")
        plt.xlabel("$F_1$")
        plt.ylabel("$F_2$")
        plt.title('Fronteira de Pareto', fontweight="bold")
       
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        plt.close() 
        buffer.seek(0)
        image_file = ContentFile(buffer.read(), name=f"pareto.png")
        graph = File.objects.create(file=image_file)
        buffer.close()

        self.charts.files.add(
            graph
        )

    def average_parameter_by_generation(self, parameter, parameter_name):

        mean_by_gen = self.df.groupby('gen')[parameter].mean().reset_index()

        # Plotando o gráfico
        plt.figure(figsize=(8, 6))
        plt.plot(mean_by_gen['gen'], mean_by_gen[parameter], linestyle='-', color='blue', label=parameter_name)
        plt.xlabel('Geração')
        plt.ylabel(parameter_name)
        plt.title(f'{parameter_name} por Geração', fontweight="bold")
        plt.legend()
       
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        plt.close() 
        buffer.seek(0)
        image_file = ContentFile(buffer.read(), name=f"f1Xgen.png")
        graph = File.objects.create(file=image_file)
        buffer.close()

        self.charts.files.add(
            graph
        )

    def media_fatores_correcao_por_geracao(self):

        params = ['jl', 'js', 'jb', 'jr', 'jc']
        colors = ['red', 'green', 'yellow', 'orange', 'blue']
        mean_by_gen = self.df.groupby('gen')[params].mean().reset_index()


        plt.figure(figsize=(8, 6))

        for i, param in enumerate(params):
            plt.plot(mean_by_gen['gen'], mean_by_gen[param], linestyle='-', color=colors[i], label=param)

        plt.xlabel('Geração')
        plt.title(f'Fatores de correção de $h_c$ por Geração', fontweight="bold")
        plt.legend()
       
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        plt.close() 
        buffer.seek(0)
        image_file = ContentFile(buffer.read(), name=f"correcaoXgen.png")
        graph = File.objects.create(file=image_file)
        buffer.close()

        self.charts.files.add(
            graph
        )

    def process_all_graphs(self):
        if self.nsga2:
            self.pareto_front_chart()
            self.average_parameter_by_generation('objective_function_2', r'Média de $F_2$')
        
        self.media_fatores_correcao_por_geracao()
        self.average_parameter_by_generation('delta_PT', r'Média de $\Delta P_t$')
        self.average_parameter_by_generation('delta_Ps', r'Média de $\Delta P_c$')
        self.average_parameter_by_generation('A_proj', r'Média de $A_{proj}$')

        self.average_parameter_by_generation('hio', r'Média de $h_{io}$')
        self.average_parameter_by_generation('hs', r'Média de $h_{c}$')
        self.average_parameter_by_generation('A_proj', r'Média de $A_{proj}$')

        self.average_parameter_by_generation('objective_function_1', r'Média de $F_1$')
        self.average_parameter_by_generation('L', 'Média de L')
        self.average_parameter_by_generation('lc', 'Média do $L_c$')
        self.average_parameter_by_generation('ls', 'Média da $L_s$')


        self.save_data_as_csv()
        
       

