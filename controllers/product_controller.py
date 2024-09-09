from flask import jsonify, request
from models.product import add_product, get_products, get_product, update_product, delete_product


def create_product():
    data = request.get_json()
    id = add_product(data)
    return id, 201


def read_products():
    products = get_products()
    if products:
        return jsonify({"products": products}), 200
    else:
        return jsonify({"error": "Product not found"}), 404


def read_product(id):
    product = get_product(id)
    if product:
        return jsonify({"product": product}), 200
    else:
        return jsonify({"error": "Product not found"}), 404


def modify_product(id):
    data = request.get_json()
    if data:
        product_id = update_product(id, data)
        if product_id:
            return jsonify({"message": "Product updated successfully"}), 200
        else:
            return jsonify({"error": "Product not found"}), 404


def remove_product(id):
    exists = get_product(id)
    if exists:
        delete_product(id)
        return jsonify({"message": "Product deleted successfully"}), 200
    else:
        return jsonify({"error": "Product not found"}), 404
