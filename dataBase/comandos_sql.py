import sqlite3
from dataBase.constants import *
import openpyxl
POL2M = 0.0254

def conect_sqlite(data_base, query = None):
    banco = sqlite3.connect(data_base)
    cursor = banco.cursor()
    if query != None:
        cursor.execute(query)
    banco.commit()
    return cursor

def filtro_sqlite(cursor, query, one = False):
   
    cursor.execute(query)
    #print(cursor.fetchall())
    #cursor.commit()
    if one:
        result = cursor.fetchone()
    else:
        result = cursor.fetchall()
    return result


if __name__ == "__main__":
    # connect(DB_CONSTANTS_CASCO_TUBO, "CREATE TABLE Constantes_a(angulo_a_tubos INTEGER, Res_max INTEGER, Res_min INTEGER, a1 DOUBLE, a2 DOUBLE, a3 DOUBLE, a4 DOUBLE)")
    # connect(DB_CONSTANTS_CASCO_TUBO, "DROP TABLE Constantes_a") 
    # comandos_sqlite(DB_CONSTANTS_CASCO_TUBO, f"INSERT INTO Constantes_a VALUES({a_t}, {Re_max}, {Re_min}, {a1}, {a2}, {a3}, {a4})")  
    
    cursor = conect_sqlite(DB_CONSTANTS_CASCO_TUBO)
    
    query  = "SELECT * FROM Contagem_de_tubos WHERE Np_4 =51"

    linhas = filtro_sqlite(cursor, query)

    for lin in linhas:
        for x in lin:
            print(x)