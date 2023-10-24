import sqlite3
#from constants import *
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
    #conect_sqlite(DB_CONSTANTS_DIR, "CREATE TABLE Delta_sb(D_nominal_min DOUBLE, D_nominal_max DOUBLE, delta_sb DOUBLE)")
    # conect_sqlite(DB_CONSTANTS_DIR, "DROP TABLE Delta_sb") 

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
    
    # Dc = 1

    # cursor = conect_sqlite(DB_CONSTANTS_DIR)
    # sql_linha = f"SELECT d_bocal FROM Diametro_bocal WHERE D_casco_min <= {Dc} AND D_casco_max >= {Dc} "
    # linha = filtro_sqlite(cursor, sql_linha, True)

    # print(linha[0])

    # angulo_tubo = 30
    # Res = 100
    
    Dn = 0.3

    cursor = conect_sqlite(DB_CONSTANTS_DIR)
    sql_linha = f"SELECT delta_sb FROM Delta_sb WHERE D_nominal_min <= {Dn} AND D_nominal_max >= {Dn} "
    linha = filtro_sqlite(cursor, sql_linha, True)

    print(linha)