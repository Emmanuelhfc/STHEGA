import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from django.core.files.base import ContentFile
from API.models import File, Charts

class DataProcessor:
    def __init__(self, data, calcultion_id):
        self.df = pd.DataFrame(data)
        self.calcultion_id = calcultion_id
        last_gen_number = self.df['gen'].max()
        self.last_gen_data = self.df[self.df['gen'] == last_gen_number]

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
    
    def pareto_front(self):
        plt.figure(figsize=(8, 6))
        plt.scatter(self.last_gen_data['objective_function_1'], self.last_gen_data['objective_function_2'], facecolor="none", edgecolor="red")
        plt.xlabel("F1")
        plt.ylabel("F2")
        plt.grid(True)
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        plt.close() 
        buffer.seek(0)
        image_file = ContentFile(buffer.read(), name=f"pareto.png")
        graph = File.objects.create(file=image_file)
        buffer.close()

        return graph

    def process_all_graphs(self):

        charts = Charts.objects.create(calculation_id = self.calcultion_id)
        charts.files.add(
            self.pareto_front()
        )

