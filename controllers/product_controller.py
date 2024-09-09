from flask import jsonify, request
from models.product import add_product, get_products, get_product, update_product, delete_product
from utils.index import validade_product_data


def create_product():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Product data is required."}), 400
        is_valid, error = validade_product_data(data)
        if not is_valid:
            return jsonify({"error": error}), 400
        id = add_product(data)
        return id, 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def read_products():
    try:
        products = get_products()
        if products:
            return jsonify({"products": products}), 200
        else:
            return jsonify({"error": "Product not found."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def read_product(id):
    try:
        product = get_product(id)
        if product:
            return jsonify({"product": product}), 200
        else:
            return jsonify({"error": "Product not found."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def modify_product(id):
    try:
        exists = get_product(id)
        if not exists:
            return jsonify({"error": "Product not found."}), 404

        data = request.get_json()
        if not data:
            return jsonify({"error": "No product data provided."}), 400

        is_valid, error = validade_product_data(data)
        if not is_valid:
            return jsonify({"error": error}), 400

        update_product(id, data)
        return jsonify({"message": "Product updated successfully."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def remove_product(id):
    try:
        exists = get_product(id)
        if exists:
            delete_product(id)
            return jsonify({"message": "Product deleted successfully"}), 200
        else:
            return jsonify({"error": "Product not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
