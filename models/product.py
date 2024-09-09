from config.database import execute
from entities.product import Product
from utils.index import validade_product_data
from uuid import uuid4


def add_product(data):
    is_valid, error = validade_product_data(data)
    if error:
        return {'error': error}
    query = "INSERT INTO products (id, name, description, price) VALUES (%s, %s, %s, %s)"
    product_id = str(uuid4())
    try:
        product_id = execute(
            query, (product_id, data["name"], data["description"], data["price"]))
        return {"success": True, "id": product_id}
    except Exception as e:
        print("ERRO AQUI")
        return {"error": str(e)}


def get_products():
    query = "SELECT * FROM products"
    try:
        products = execute(query, params=None)
        print(products)
        return [Product(*product).__dict__ for product in products]
    except Exception as e:
        return {"error": str(e)}


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
