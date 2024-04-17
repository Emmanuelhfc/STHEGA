import sqlalchemy

def engine():
    return sqlalchemy.create_engine("sqlite:///dataBase/db.sqlite3", echo=True)