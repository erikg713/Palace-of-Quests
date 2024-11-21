from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from ..models import User, db

bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route("/register", methods=["POST"])
def register():
    data = request.json
    hashed_password = generate_password_hash(data["password"])
    user = User(
        username=data["username"],
        email=data["email"],
        password_hash=hashed_password
    )
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201

@bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(email=data["email"]).first()
    if user and check_password_hash(user.password_hash, data["password"]):
        access_token = create_access_token(identity=user.user_id)
        return jsonify({"access_token": access_token}), 200
    return jsonify({"error": "Invalid credentials"}), 401
from flask import Blueprint, request, jsonify
import requests
import os
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User, db
from app.utils.security import create_jwt

auth_bp = Blueprint("auth", __name__)

# Pi Network API setup
PI_API_BASE_URL = "https://api.minepi.com/v2"
PI_API_KEY = os.getenv("PI_API_KEY")

@auth_bp.route("/signin", methods=["POST"])
def signin():
    # Extract access token from request data
    access_token = request.json.get("authResult", {}).get("accessToken")
    if not access_token:
        return jsonify({"error": "Access token is required"}), 400

    headers = {"Authorization": f"Bearer {access_token}"}
    try:
        # Send a request to the Pi Network API to verify the access token
        response = requests.get(f"{PI_API_BASE_URL}/me", headers=headers)
        response.raise_for_status()

        # Return user data if successful
        return jsonify(response.json())

    except requests.exceptions.HTTPError as http_err:
        # Handle API-specific errors
        print(f"HTTP error occurred: {http_err}")
        return jsonify({"error": "User verification failed"}), 401
    except Exception as err:
        # Handle unexpected errors
        print(f"Unexpected error: {err}")
        return jsonify({"error": "An unexpected error occurred"}), 500

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = generate_password_hash(data['password'])
    user = User(username=data['username'], password_hash=hashed_password)
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User registered successfully!"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and check_password_hash(user.password_hash, data['password']):
        token = create_jwt({"user_id": user.id})
        response = jsonify({"message": "Logged in successfully"})
        response.set_cookie("access_token", token, httponly=True, secure=True)
        return response, 200
    return jsonify({"error": "Invalid credentials"}), 401