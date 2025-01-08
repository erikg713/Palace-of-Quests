from flask import Blueprint, request, jsonify
from app.models import db, User
from app.utils.jwt_utils import generate_jwt, decode_jwt
from bcrypt import hashpw, gensalt, checkpw

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    hashed_password = hashpw(password.encode('utf-8'), gensalt())
    new_user = User(username=username, password=hashed_password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if not user or not checkpw(password.encode('utf-8'), user.password):
        return jsonify({"error": "Invalid username or password"}), 401

    token = generate_jwt({"user_id": user.id})
    return jsonify({"token": token}), 200