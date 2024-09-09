import mysql.connector
from uuid import uuid4

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="products"
)

cursor = db.cursor()


def execute(query, params: None):
    try:
        cursor.execute(query, params)
        db.commit()
        return cursor.fetchall() if query.strip().lower().startswith("select") else cursor.lastrowid
    except Exception as e:
        db.rollback()
        return {"error": str(e)}


cursor.execute("DROP DATABASE IF EXISTS products;")
cursor.execute("CREATE DATABASE products;")
cursor.execute("USE products;")

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS products (
        id CHAR(36) PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        description TEXT,
        price DECIMAL(10, 2) NOT NULL
    );
    """
)

cursor.execute(
    """INSERT INTO products (id, name, description, price)
    VALUES (%s, %s, %s, %s)""", (str(uuid4()), "Product 3", "Description for Product 3", 10.99)
)
db.commit()
