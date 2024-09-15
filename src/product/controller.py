from flask import Blueprint, request, jsonify
from config.database import get_db_connection

product_bp = Blueprint("product", __name__)


@product_bp.route("/", methods=["GET"])
def get_products():
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()
        conn.close()
        return jsonify(rows)
    else:
        return jsonify({"error": "Failed to connect to the database."}), 500
