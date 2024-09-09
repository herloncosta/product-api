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
        execute(
            query, (product_id, data["name"], data["description"], data["price"]), fetch=False)
        return {"success": True, "id": product_id}
    except Exception as e:
        print("ERRO AQUI")
        return {"error": str(e)}


def get_products():
    query = "SELECT * FROM products"
    try:
        products = execute(query, params=None, fetch=True)
        result = [Product(*product).__dict__ for product in products]
        return result
    except Exception as e:
        return {"error": str(e)}


def get_product(id):
    query = "SELECT * FROM products WHERE id = %s"
    try:
        product = execute(query, (id,), fetch=True)
        if product:
            return Product(*product[0]).__dict__
        else:
            return None
    except Exception as e:
        return {"error": str(e)}


def update_product(id, data):
    if not data or not id:
        return {"error": "Product ID and data are required."}
    is_valid, error = validade_product_data(data)
    if not is_valid:
        return {"error": error}
    query = "UPDATE products SET name = %s, description = %s, price = %s WHERE id = %s"
    try:
        execute(
            query, (data["name"], data["description"], data["price"], id))
        return {"success": True}
    except Exception as e:
        return {"error": str(e)}


def delete_product(id):
    query = "DELETE FROM products WHERE id = %s"
    try:
        execute(query, (id,))
        return {"success": True}
    except Exception as e:
        return {"error": str(e)}
