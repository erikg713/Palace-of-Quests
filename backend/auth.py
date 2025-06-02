from flask import Blueprint, request, jsonify, make_response, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from app.utils.security import create_jwt, jwt_required
from app.models import User, db
from sqlalchemy.exc import IntegrityError
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

auth_bp = Blueprint('auth', __name__)
limiter = Limiter(key_func=get_remote_address)

# Register a new user
@auth_bp.route('/register', methods=['POST'])
@limiter.limit("5 per minute")  # Rate limit to prevent abuse
def register():
    """
    Registers a new user.
    Request JSON: { "username": "string", "password": "string" }
    """
    data = request.get_json()

    # Validate input
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({"error": "Username and password are required"}), 400

    if len(data['password']) < 8:
        return jsonify({"error": "Password must be at least 8 characters long"}), 400

    # Hash the password and save the user
    hashed_password = generate_password_hash(data['password'])
    user = User(username=data['username'], password_hash=hashed_password)

    try:
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "User registered successfully!"}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Username already exists"}), 409

# User login
@auth_bp.route('/login', methods=['POST'])
@limiter.limit("10 per minute")  # Rate limit to prevent brute force attacks
def login():
    """
    Logs in a user and sets a secure JWT token as a cookie.
    Request JSON: { "username": "string", "password": "string" }
    """
    data = request.get_json()

    # Validate input
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({"error": "Username and password are required"}), 400

    # Find the user
    user = User.query.filter_by(username=data['username']).first()

    # Check credentials
    if user and check_password_hash(user.password_hash, data['password']):
        token = create_jwt({"user_id": user.id}, expires_in=3600)  # Token expires in 1 hour
        response = make_response(jsonify({"message": "Logged in successfully"}))
        response.set_cookie(
            "access_token",
            token,
            httponly=True,
            secure=current_app.config.get('ENV') == 'production',
            samesite='Strict' if current_app.config.get('ENV') == 'production' else None
        )
        return response, 200

    return jsonify({"error": "Invalid credentials"}), 401
