import pandas as pd
import matplotlib.pyplot as plt
from pymoo.visualization.scatter import Scatter
from io import BytesIO
from django.core.files.base import ContentFile
from API.models import File, Charts

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
        
        # Salva a imagem no modelo Django
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
        plt.xlabel("F1")
        plt.ylabel("F2")
        plt.title('Fronteira de Pareto')
       
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

    def process_all_graphs(self):
        self.save_data_as_csv()
        if self.nsga2:
            self.pareto_front_chart()
       

