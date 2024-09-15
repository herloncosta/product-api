from config.database import get_db_connection
from .model import Product


def get_all_products():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()
        if rows:
            return rows
        else:
            return []
    except Exception as err:
        print("Error fetching products", err)
        return None
    finally:
        if conn:
            cursor.close()
            conn.close()


def get_product(id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM products WHERE id = %s", (id,))
        row = cursor.fetchone()
        return Product(row['id'], row['name'], row['description'], row['price'])
    except Exception as err:
        print("Error fetching product", err)
        return None
    finally:
        if conn:
            cursor.close()
            conn.close()


def create_product(id, name, description, price):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO products (id, name, description, price) VALUES (%s, %s, %s, %s)", (id, name, description, price))
        conn.commit()
    except Exception as err:
        print("Error inserting product", err)
        return None
    finally:
        if conn:
            cursor.close()
            conn.close()


def update_product(id, name, description, price):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE products SET name = %s, description = %s, price = %s WHERE id = %s",
                       (name, description, price, id))
        conn.commit()
    except Exception as err:
        print("Error updating product", err)
        return None
    finally:
        if conn:
            cursor.close()
            conn.close()


def remove_product(id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM products WHERE id = %s", (id,))
        conn.commit()
    except Exception as err:
        print("Error deleting product", err)
        return None
    finally:
        if conn:
            cursor.close()
            conn.close()
