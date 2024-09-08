from flask import Blueprint
from controllers.product_controller import create_product, read_products, read_product, modify_product, remove_product

products_router = Blueprint("products", __name__)

products_router.route("/products", methods=["POST"])(create_product)
products_router.route("/products/", methods=["GET"])(read_products)
products_router.route("/products/<id>", methods=["GET"])(read_product)
products_router.route("/products/<id>",
                      methods=["PUT"])(modify_product)
products_router.route("/products/<id>", methods=["DELETE"])(remove_product)
