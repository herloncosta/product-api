from config.database import get_db_connection, close_db_connection
from .model import User


def get_all_users():
    db = None
    try:
        db = get_db_connection()
        if not db:
            raise Exception("Falha ao conectar ao banco de dados")
        
        cursor = db.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users")
        result = cursor.fetchall()
        return result
    except Exception as err:
        print("Erro ao buscar usuários:", err)
        return None
    finally:
        if db:
            close_db_connection(db)


def get_user(id):
    db = None
    try:
        db = get_db_connection()
        cursor = db.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
        row = cursor.fetchone()
        return User(row['id'], row['name'], row['email'], row['password'], row['role'])
    except Exception as err:
        print("Error fetching user", err)
        return None
    finally:
        if db:
            close_db_connection(db)


def create_user(id, name, email, password, role):
    try:
        db = get_db_connection()
        cursor = db.connection.cursor()
        cursor.execute(
            "INSERT INTO users (id, name, email, password, role) VALUES (%s, %s, %s, %s, %s)", (id, name, email, password, role))
        db.connection.commit()
        return True
    except Exception as err:
        print("Erro ao inserir usuário:", err)
        return False
    finally:
        if db:
            close_db_connection(db)


def update_user(id, name, email, password, role):
    try:
        db = get_db_connection()
        cursor = db.connection.cursor()
        cursor.execute("UPDATE users SET name = %s, email = %s, password = %s, role = %s WHERE id = %s",
                       (name, email, password, role, id))
        db.commit()
    except Exception as err:
        print("Error updating user", err)
        return False
    finally:
        if db:
            close_db_connection(db)


def remove_user(id):
    try:
        db = get_db_connection()
        cursor = db.connection.cursor()
        cursor.execute("DELETE FROM users WHERE id = %s", (id,))
        db.connection.commit()
        return True
    except Exception as err:
        print("Erro ao deletar usuário:", err)
        return False
    finally:
        if db:
            close_db_connection(db)
