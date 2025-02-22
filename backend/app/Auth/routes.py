# auth/routes.py
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from datetime import timedelta, datetime
import secrets
from models import User, PasswordReset
from . import db, mail
from validators import validate_password, validate_username
from flask_mail import Message
import re

auth_bp = Blueprint("auth", __name__)

# Initialize rate limiter
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["100 per day", "5 per minute"]
)

@auth_bp.route('/register', methods=['POST'])
@limiter.limit("5 per hour")
def register():
    try:
        data = request.get_json()
        
        # Enhanced input validation
        required_fields = ['username', 'password', 'email']
        if not all(key in data for key in required_fields):
            return jsonify({"error": "Missing required fields"}), 400
            
        # Email validation
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', data['email']):
            return jsonify({"error": "Invalid email format"}), 400
            
        # Username and password validation
        if not validate_username(data['username']):
            return jsonify({"error": "Invalid username format"}), 400
            
        if not validate_password(data['password']):
            return jsonify({"error": "Password does not meet security requirements"}), 400
            
        # Check existing user
        if User.query.filter(
            db.or_(
                User.username == data['username'].lower(),
                User.email == data['email'].lower()
            )
        ).first():
            return jsonify({"error": "Username or email already exists"}), 409
            
        # Create new user with enhanced security
        hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256:260000')
        new_user = User(
            username=data['username'].lower(),
            email=data['email'].lower(),
            password=hashed_password,
            email_verified=False,
            verification_token=secrets.token_urlsafe(32)
        )
        
        db.session.add(new_user)
        db.session.commit()
        
        # Send verification email
        send_verification_email(new_user)
        
        return jsonify({
            "message": "User registered successfully. Please check your email to verify your account.",
            "user_id": new_user.id
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Registration failed"}), 500

@auth_bp.route('/login', methods=['POST'])
@limiter.limit("10 per minute")
def login():
    try:
        data = request.get_json()
        
        # Input validation
        if not all(key in data for key in ['username', 'password']):
            return jsonify({"error": "Missing required fields"}), 400
            
        user = User.query.filter_by(username=data['username'].lower()).first()
        
        # Enhanced security checks
        if user:
            if user.login_attempts >= 5 and (datetime.utcnow() - user.last_failed_login).total_seconds() < 300:
                return jsonify({"error": "Account temporarily locked. Please try again later"}), 429
                
            if not user.is_active:
                return jsonify({"error": "Account is deactivated"}), 403
                
            if not user.email_verified:
                return jsonify({"error": "Please verify your email before logging in"}), 403
        
        if not user or not check_password_hash(user.password, data['password']):
            if user:
                user.login_attempts += 1
                user.last_failed_login = datetime.utcnow()
                db.session.commit()
            return jsonify({"error": "Invalid credentials"}), 401
            
        # Reset login attempts on successful login
        user.login_attempts = 0
        user.last_login = datetime.utcnow()
        db.session.commit()
        
        # Create tokens with refresh capability
        access_token = create_access_token(
            identity=user.id,
            expires_delta=timedelta(hours=1)
        )
        refresh_token = create_access_token(
            identity=user.id,
            expires_delta=timedelta(days=30),
            additional_claims={"refresh": True}
        )
        
        return jsonify({
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "Bearer",
            "expires_in": 3600
        }), 200
        
    except Exception as e:
        return jsonify({"error": "Login failed"}), 500

@auth_bp.route('/verify-email/<token>', methods=['GET'])
def verify_email(token):
    try:
        user = User.query.filter_by(verification_token=token).first()
        if not user:
            return jsonify({"error": "Invalid verification token"}), 400
            
        user.email_verified = True
        user.verification_token = None
        db.session.commit()
        
        return jsonify({"message": "Email verified successfully"}), 200
        
    except Exception as e:
        return jsonify({"error": "Email verification failed"}), 500

@auth_bp.route('/forgot-password', methods=['POST'])
@limiter.limit("3 per hour")
def forgot_password():
    try:
        data = request.get_json()
        if 'email' not in data:
            return jsonify({"error": "Email is required"}), 400
            
        user = User.query.filter_by(email=data['email'].lower()).first()
        if not user:
            # Return success even if user doesn't exist to prevent email enumeration
            return jsonify({"message": "If your email is registered, you will receive a password reset link"}), 200
            
        # Create password reset token
        reset_token = secrets.token_urlsafe(32)
        password_reset = PasswordReset(
            user_id=user.id,
            token=reset_token,
            expires_at=datetime.utcnow() + timedelta(hours=1)
        )
        
        db.session.add(password_reset)
        db.session.commit()
        
        # Send password reset email
        send_password_reset_email(user, reset_token)
        
        return jsonify({"message": "If your email is registered, you will receive a password reset link"}), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Password reset request failed"}), 500

@auth_bp.route('/reset-password/<token>', methods=['POST'])
def reset_password(token):
    try:
        data = request.get_json()
        if 'new_password' not in data:
            return jsonify({"error": "New password is required"}), 400
            
        if not validate_password(data['new_password']):
            return jsonify({"error": "Password does not meet security requirements"}), 400
            
        reset = PasswordReset.query.filter_by(
            token=token,
            used=False
        ).first()
        
        if not reset or reset.expires_at < datetime.utcnow():
            return jsonify({"error": "Invalid or expired reset token"}), 400
            
        user = User.query.get(reset.user_id)
        if not user:
            return jsonify({"error": "User not found"}), 404
            
        # Update password and invalidate reset token
        user.password = generate_password_hash(data['new_password'], method='pbkdf2:sha256:260000')
        reset.used = True
        db.session.commit()
        
        return jsonify({"message": "Password reset successful"}), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Password reset failed"}), 500

@auth_bp.route('/me', methods=['GET'])
@jwt_required()
def get_user_profile():
    try:
        current_user_id = get_jwt_identity()
        user = User.query.get(current_user_id)
        
        if not user:
            return jsonify({"error": "User not found"}), 404
            
        if not user.is_active:
            return jsonify({"error": "Account is deactivated"}), 403
            
        return jsonify({
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "created_at": user.created_at.isoformat(),
            "last_login": user.last_login.isoformat() if user.last_login else None
        }), 200
        
    except Exception as e:
        return jsonify({"error": "Failed to fetch user profile"}), 500

# Helper functions
def send_verification_email(user):
    verification_url = f"{request.host_url}verify-email/{user.verification_token}"
    msg = Message(
        "Verify your email",
        recipients=[user.email],
        body=f"Please click the following link to verify your email: {verification_url}"
    )
    mail.send(msg)

def send_password_reset_email(user, token):
    reset_url = f"{request.host_url}reset-password/{token}"
    msg = Message(
        "Password Reset Request",
        recipients=[user.email],
        body=f"Please click the following link to reset your password: {reset_url}"
    )
    mail.send(msg)
