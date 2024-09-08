import mysql.connector

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
        if query.startswith("INSERT"):
            db.commit()
            return cursor.lastrowid
        elif query.startswith("SELECT"):
            return cursor.fetchall()
        else:
            db.commit()
            return
    except mysql.connector.Error as error:
        print("Error executing query:", error)
        return False

# cursor.execute(
#     """
#     CREATE TABLE IF NOT EXISTS products (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         name VARCHAR(255) NOT NULL,
#         description TEXT,
#         price DECIMAL(10, 2) NOT NULL
#     )
#     """
# )

# cursor.execute(
#     """INSERT INTO products (name, description, price)
#     VALUES (%s, %s, %s)""", ("Product 3", "Description for Product 3", 10.99)
# )
# db.commit()

# cursor.execute("SELECT * FROM products.products")
# result = cursor.fetchall()

# for row in result:
#     print(row)
