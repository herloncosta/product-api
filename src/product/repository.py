from config.database import get_db_connection


def get_all_products():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()
        conn.close()
        return rows
    else:
        return None
