from config.database import execute
from entities.product import Product


def add_product(data):
    query = "INSERT INTO products (name, description, price) VALUES (%s, %s, %s)"
    product_id = execute(
        query, (data["name"], data["description"], data["price"]))
    return product_id


def get_products():
    query = "SELECT * FROM products"
    products = execute(query, params=None)

    result = []
    for row in products:
        product = Product(*row)  # unpacking
        result.append(product.__dict__)
    return result


def get_product(id):
    query = "SELECT * FROM products WHERE id = %s"
    product = execute(query, (id,))

    if product:
        return Product(*product[0]).__dict__
    else:
        return None


def update_product(id, data):
    if not data or not id:
        return None
    query = "UPDATE products SET name = %s, description = %s, price = %s WHERE id = %s"
    product_id = execute(
        query, (data["name"], data["description"], data["price"], id))
    return product_id


def delete_product(id):
    query = "DELETE FROM products WHERE id = %s"
    data = execute(query, (id,))
    print(data)
    return True
