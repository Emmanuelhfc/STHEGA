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
    # conect_sqlite(DB_CONSTANTS_DIR, "CREATE TABLE Delta_sb(Dn_min DOUBLE, Dn_max DOUBLE, delta_sb DOUBLE)")
    # conect_sqlite(DB_CONSTANTS_DIR, "DROP TABLE Delta_sb")
    # 
    Dn = 1.3 
    cursor = conect_sqlite(DB_CONSTANTS_DIR)
    sql_linha = f"SELECT delta_sb FROM Delta_sb WHERE Dn_min <= {Dn} AND Dn_max >= {Dn} "
    linha = filtro_sqlite(cursor, sql_linha)

    print(linha)
    