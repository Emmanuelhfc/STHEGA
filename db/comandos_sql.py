import sqlite3
from constants import *
import openpyxl
POL2M = 0.0254
def connect(data_base, SQL):
    banco = sqlite3.connect(data_base)
    cursor = banco.cursor()
    cursor.execute(SQL)
    banco.commit()
    return cursor


if __name__ == "__main__":
    # connect(DB_CONSTANTS_CASCO_TUBO, "CREATE TABLE Constantes_a(angulo_a_tubos INTEGER, Res_max INTEGER, Res_min INTEGER, a1 DOUBLE, a2 DOUBLE, a3 DOUBLE, a4 DOUBLE)")
    # connect(DB_CONSTANTS_CASCO_TUBO, "DROP TABLE Constantes_a") 
        
    excel = r"C:\Users\carvalhoe\Documents\GITHUB\HeatExGA\base_dados.xlsx"
    workbook = openpyxl.load_workbook(excel)
    planilha = workbook["SQL"]

    cont =1
    for linha in planilha.iter_rows(min_row=1, values_only=True):  # Começa da segunda linha, assumindo que a primeira linha é o cabeçalho
    # Acesse os valores das colunas
        a_t, Re_max, Re_min, a1, a2, a3, a4 = linha[0], linha[1], linha[2], linha[3], linha[4], linha[5], linha[6]




        connect(DB_CONSTANTS_CASCO_TUBO, f"INSERT INTO Constantes_a VALUES({a_t}, {Re_max}, {Re_min}, {a1}, {a2}, {a3}, {a4})")
   
        
        if cont >=15:
            break
        cont = cont + 1

    # Feche o arquivo Excel
    workbook.close() 
   
