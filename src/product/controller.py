from flask import Blueprint, request, jsonify
from config.database import get_db_connection
from .service import fetch_all_products, add_product
from uuid import uuid4

product_bp = Blueprint("product", __name__)


@product_bp.route("/", methods=["GET"])
def get_products():
    products = fetch_all_products()
    if products:
        return jsonify(products), 200


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
