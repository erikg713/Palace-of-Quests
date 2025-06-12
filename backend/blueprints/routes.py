from flask import Blueprint, request, jsonify, abort, current_app
from werkzeug.exceptions import HTTPException

routes_bp = Blueprint("routes", __name__)

@routes_bp.route("/", methods=["GET"])
def home():
    """API welcome route."""
    return jsonify(message="Welcome to Palace of Quests API"), 200

@routes_bp.route("/health", methods=["GET"])
def health_check():
    """Health check endpoint."""
    return jsonify(status="healthy"), 200

@routes_bp.route("/example", methods=["POST"])
def example_post():
    """Example POST endpoint with input validation."""
    data = request.get_json(silent=True)
    if not data or not isinstance(data, dict) or not data.get("name"):
        return jsonify(error="Missing 'name' in request body."), 400

    # Example processing (replace with real logic)
    return jsonify(greeting=f"Hello, {data['name']}!"), 201

@routes_bp.errorhandler(Exception)
def handle_exception(e):
    """Global error handler for the blueprint."""
    code = 500
    default_message = "An internal error occurred. Please try again later."
    if isinstance(e, HTTPException):
        code = e.code
        message = e.description
    else:
        message = default_message

    # Optional: log errors in production
    if current_app and hasattr(current_app, "logger"):
        current_app.logger.error("Exception: %s", e, exc_info=True)

    return jsonify(error=message), code

# To use this blueprint, register it in your main app:
# from backend.blueprints.routes import routes_bp
# app.register_blueprint(routes_bp, url_prefix='/api')
