from flask import Blueprint, request, jsonify
from .service import fetch_all_products, add_product, fetch_product, modify_product
from uuid import uuid4

product_bp = Blueprint("product", __name__)


@product_bp.route("/", methods=["GET"])
def get_products():
    products = fetch_all_products()
    if products:
        return jsonify(products), 200


@product_bp.route("/<product_id>", methods=["GET"])
def get_product(product_id):
    product = fetch_product(product_id)
    if product:
        return jsonify(product.to_dict()), 200
    else:
        return jsonify({'error': 'Product not found'}), 404


@product_bp.route("/", methods=["POST"])
def create_product():
    id = str(uuid4())
    name = request.json.get('name')
    description = request.json.get('description')
    price = request.json.get('price')

    if name and description and price:
        add_product(id, name, description, price)
        return jsonify({'message': 'Product created successfully', "id": id}), 201
    else:
        return jsonify({'error': 'Failed to connect to the database'}), 500


@product_bp.route("/<product_id>", methods=["PUT"])
def update_product(product_id):
    product = fetch_product(product_id)

    if product:
        name = request.json.get('name')
        description = request.json.get('description')
        price = request.json.get('price')

        if name or description or price:
            modify_product(product_id, name, description, price)
            return jsonify({'message': 'Product updated successfully'}), 200
        else:
            return jsonify({'error': 'No changes provided'}), 400
    else:
        return jsonify({'error': 'Product not found'}), 404
