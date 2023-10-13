import sqlite3
from constants import *
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
    #conect_sqlite(DB_CONSTANTS_DIR, "CREATE TABLE Passos_tubos(de DOUBLE, p DOUBLE, a_tubos TEXT, pp DOUBLE, pn DOUBLE)")
    # connect(DB_CONSTANTS_CASCO_TUBO, "DROP TABLE Constantes_a") 

    de = 0.750 * POL2M
    p = 1 * POL2M
    a_tubos = "triangular"
    pp = 0.866 * POL2M
    pn = 0.884 * POL2M

    npt = "NP_1"
    a_tubos = 'triangular 1 pol'
    Ds = 0.254
    de = 0.01905
    cursor = conect_sqlite(DB_CONSTANTS_DIR)
    sql_NT = f"SELECT {npt} FROM Contagem_de_tubos WHERE a_tubos = '{a_tubos}' AND Ds_m = {Ds} AND d_m = {de}"
    sql_Dotl = f"SELECT Dotl_m FROM Contagem_de_tubos WHERE a_tubos = '{a_tubos}' AND Ds_m = {Ds} AND d_m = {de}"

    Nt = filtro_sqlite(cursor, sql_NT, True)
    Dotl = filtro_sqlite(cursor, sql_Dotl, True)

    print(Nt)
    print(Dotl)
    #conect_sqlite(DB_CONSTANTS_DIR, f"INSERT INTO Passos_tubos VALUES({de}, {p}, '{a_tubos}', {pp}, {pn})")  
    
    