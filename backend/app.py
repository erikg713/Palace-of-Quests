import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from blueprints.auth import auth_bp
from blueprints.levels import levels_bp
from blueprints.progress import progress_bp
from utils.jwt import JWTManager
from config import Config

# Initialize Flask app
app = Flask(__name__)

# Load configuration
app.config.from_object(Config)

# CORS setup (for allowing frontend and backend communication)
CORS(app, resources={r"/*": {"origins": "*"}})

# Rate limiting for security
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"]
)

# JWT setup
jwt = JWTManager(app)

# Register Blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(levels_bp, url_prefix='/levels')
app.register_blueprint(progress_bp, url_prefix='/progress')

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
