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
        
def criar_tabela_users():
    db = None
    try:
        db = get_db_connection()
        if not db:
            raise Exception("Falha ao conectar ao banco de dados")
        
        cursor = db.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id VARCHAR(36) PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                password VARCHAR(255) NOT NULL,
                role VARCHAR(50)
            )
        """)
        db.connection.commit()
        print("Tabela 'users' criada com sucesso!")
    except Exception as err:
        print(f"Erro ao criar tabela 'users': {err}")
    finally:
        if db:
            close_db_connection(db)

def criar_tabela_products():
    db = None
    try:
        db = get_db_connection()
        if not db:
            raise Exception("Falha ao conectar ao banco de dados")
        
        cursor = db.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id VARCHAR(36) PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                description TEXT,
                price DECIMAL(10, 2) NOT NULL
            )
        """)
        db.connection.commit()
        print("Tabela 'products' criada com sucesso!")
    except Exception as err:
        print(f"Erro ao criar tabela 'products': {err}")
    finally:
        if db:
            close_db_connection(db)

def rollback_database():
    db = None
    try:
        db = get_db_connection()
        if not db:
            raise Exception("Falha ao conectar ao banco de dados")

        cursor = db.connection.cursor()
        cursor.execute("DROP DATABASE IF EXISTS products")
        cursor.execute("DROP DATABASE IF EXISTS users")
        db.connection.commit()
        print("Banco de dados 'users' e 'products' deletado com sucesso!")
    except Exception as err:
        print(f"Erro ao deletar banco de dados 'users' e 'products': {err}")
    finally:
        if db:
            close_db_connection(db)