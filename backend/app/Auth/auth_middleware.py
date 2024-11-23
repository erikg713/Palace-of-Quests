from flask import request, jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity

def auth_required(fn):
    def wrapper(*args, **kwargs):
        try:
            verify_jwt_in_request()
            return fn(*args, **kwargs)
        except Exception as e:
            return jsonify({"error": "Unauthorized access", "message": str(e)}), 401
    wrapper.__name__ = fn.__name__
    return wrapper

def get_current_user():
    return get_jwt_identity()