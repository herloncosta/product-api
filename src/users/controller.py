from flask import Blueprint, request, jsonify
from uuid import uuid4
from .service import fetch_all_users, fetch_user, add_user, modify_user, delete_user

user_bp = Blueprint("user", __name__)


@user_bp.route("/", methods=["GET"])
def get_users():
    users = fetch_all_users()
    if users:
        return jsonify(users), 200
    return jsonify([]), 200


@user_bp.route("/<user_id>", methods=["GET"])
def get_user(user_id):
    user = fetch_user(user_id)
    if user:
        return jsonify(user.to_dict()), 200
    else:
        return jsonify({'error': 'User not found'}), 404


@user_bp.route("/", methods=["POST"])
def create_user():
    id = str(uuid4())
    name = request.json.get('name')
    email = request.json.get('email')
    password = request.json.get('password')
    role = request.json.get('role')

    if name and email and password:
        add_user(id, name, email, password, role)
        return jsonify({'message': 'User created successfully', "id": id}), 201
    else:
        return jsonify({'error': 'Failed to connect to the database'}), 500


@user_bp.route("/<user_id>", methods=["PUT"])
def update_user(user_id):
    user = fetch_user(user_id)

    if user:
        name = request.json.get('name')
        email = request.json.get('email')
        password = request.json.get('password')
        role = request.json.get('role')

        if name or email or password or role:
            modify_user(user_id, name, email, password, role)
            return jsonify({'message': 'User updated successfully'}), 200
        else:
            return jsonify({'error': 'No changes provided'}), 400
    else:
        return jsonify({'error': 'User not found'}), 404


@user_bp.route("/<user_id>", methods=["DELETE"])
def remove_user(user_id):
    user = fetch_user(user_id)

    if user:
        delete_user(user_id)
        return jsonify({'message': 'User deleted successfully'}), 200
    else:
        return jsonify({'error': 'User not found'}), 404
