from config.database import get_db_connection, close_db_connection
from .model import Product

def get_all_products():
    db = None
    try:
        db = get_db_connection()
        if not db:
            raise Exception("Falha ao conectar ao banco de dados")
        
        cursor = db.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM products")
        result = cursor.fetchall()
        return result
    except Exception as err:
        print("Erro ao buscar produtos:", err)
        return None
    finally:
        if db:
            close_db_connection(db)

def get_product(id):
    db = None
    try:
        db = get_db_connection()
        if not db:
            raise Exception("Falha ao conectar ao banco de dados")
        
        cursor = db.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM products WHERE id = %s", (id,))
        row = cursor.fetchone()
        if row:
            return Product(row['id'], row['name'], row['description'], row['price'])
        return None
    except Exception as err:
        print("Erro ao buscar produto:", err)
        return None
    finally:
        if db:
            close_db_connection(db)

def create_product(id, name, description, price):
    db = None
    try:
        db = get_db_connection()
        if not db:
            raise Exception("Falha ao conectar ao banco de dados")
        
        cursor = db.connection.cursor()
        cursor.execute(
            "INSERT INTO products (id, name, description, price) VALUES (%s, %s, %s, %s)",
            (id, name, description, price)
        )
        db.connection.commit()
        return True
    except Exception as err:
        print("Erro ao inserir produto:", err)
        return False
    finally:
        if db:
            close_db_connection(db)

def update_product(id, name, description, price):
    db = None
    try:
        db = get_db_connection()
        if not db:
            raise Exception("Falha ao conectar ao banco de dados")
        
        cursor = db.connection.cursor()
        cursor.execute(
            "UPDATE products SET name = %s, description = %s, price = %s WHERE id = %s",
            (name, description, price, id)
        )
        db.connection.commit()
        return True
    except Exception as err:
        print("Erro ao atualizar produto:", err)
        return False
    finally:
        if db:
            close_db_connection(db)

def remove_product(id):
    db = None
    try:
        db = get_db_connection()
        if not db:
            raise Exception("Falha ao conectar ao banco de dados")
        
        cursor = db.connection.cursor()
        cursor.execute("DELETE FROM products WHERE id = %s", (id,))
        db.connection.commit()
        return True
    except Exception as err:
        print("Erro ao remover produto:", err)
        return False
    finally:
        if db:
            close_db_connection(db)
