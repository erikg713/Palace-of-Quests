blueprint routefrom flask import Blueprint, request, jsonify, abort
from werkzeug.exceptions import HTTPException

# Initialize blueprint
routes_bp = Blueprint('routes', __name__)

# Example: Home route
@routes_bp.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to Palace of Quests API"}), 200

# Example: Health check endpoint
@routes_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

# Example: Example POST route with input validation
@routes_bp.route('/example', methods=['POST'])
def example_post():
    data = request.get_json(silent=True)
    if not data or 'name' not in data:
        abort(400, description="Missing 'name' in request body.")

    # Example processing (replace with real logic)
    response = {"greeting": f"Hello, {data['name']}!"}
    return jsonify(response), 201

# Global error handler for the blueprint
@routes_bp.errorhandler(Exception)
def handle_exception(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    return jsonify(error=str(e)), code

# To use this blueprint, register it in your main app:
# from backend.blueprints.routes import routes_bp
# app.register_blueprint(routes_bp, url_prefix='/api')
