import os
from mysql_driver.main import MySQLDriver

def get_db_connection():
    try:
        db = MySQLDriver(
            host=os.environ.get('MYSQL_HOST'),
            user=os.environ.get('MYSQL_USER'),
            password=os.environ.get('MYSQL_PASSWORD'),
            database=os.environ.get('MYSQL_DATABASE')
        )
        db.connect()
        return db
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

def close_db_connection(db):
    if db:
        db.disconnect()