import sqlite3
from constants import *
from openpyxl import load_workbook
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
    # conect_sqlite(DB_CONSTANTS_DIR, "CREATE TABLE Constantes_b(angulo_tubo DOUBLE, Re_max DOUBLE, Re_min DOUBLE, b1 DOUBLE, b2 DOUBLE, b3 DOUBLE, b4 DOUBLE)")
    # conect_sqlite(DB_CONSTANTS_DIR, "DROP TABLE Diametro_bocal") 

    # de = 0.750 * POL2M
    # p = 1 * POL2M
    # a_tubos = "triangular"
    # pp = 0.866 * POL2M
    # pn = 0.884 * POL2M

    # npt = "NP_1"
    # a_tubos = 'triangular 1 pol'
    # Ds = 0.254
    # de = 0.01905
    # cursor = conect_sqlite(DB_CONSTANTS_DIR)
    # sql_NT = f"SELECT {npt} FROM Contagem_de_tubos WHERE a_tubos = '{a_tubos}' AND Ds_m = {Ds} AND d_m = {de}"
    # sql_Dotl = f"SELECT Dotl_m FROM Contagem_de_tubos WHERE a_tubos = '{a_tubos}' AND Ds_m = {Ds} AND d_m = {de}"

    # Nt = filtro_sqlite(cursor, sql_NT, True)
    # Dotl = filtro_sqlite(cursor, sql_Dotl, True)

    # print(Nt)
    # print(Dotl)

    # pressao = 600
    # D_casco = 60
    # li = 14 + 1/2
    # lo = 23

    # D_casco = D_casco * POL2M
    # li = li * POL2M
    # lo = lo * POL2M
    
    w = load_workbook(r"C:\Users\carvalhoe\Documents\GITHUB\HeatExGA\base_dados.xlsx")

    a = w["SQL"]

    for x in range(1, 16):

        angulo = a[f"A{x}"].value
        Res_max = a[f"B{x}"].value
        Res_min = a[f"C{x}"].value
        a1 = a[f"D{x}"].value
        a2 = a[f"E{x}"].value
        a3 = a[f"F{x}"].value
        a4 = a[f"G{x}"].value

        print(f"({angulo}, {Res_max}, {Res_min}, {a1}, {a2}, {a3}, {a4})")
    
        conect_sqlite(DB_CONSTANTS_DIR, f"INSERT INTO Constantes_b VALUES({angulo}, {Res_max}, {Res_min}, {a1}, {a2}, {a3}, {a4})")
    
    