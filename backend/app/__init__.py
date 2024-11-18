from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from .config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Load configurations from the Config class
    db.init_app(app)  # Initialize the database
    JWTManager(app)  # Initialize JWTManager for token-based authentication

    # Registering Blueprints for routes
    with app.app_context():  # Ensure app context when registering blueprints
        from .routes import auth, payments, game, premium
        
        # Register each blueprint with a URL prefix
        app.register_blueprint(auth.auth_bp, url_prefix='/auth')
        app.register_blueprint(payments.payments_bp, url_prefix='/payments')
        app.register_blueprint(game.game_bp, url_prefix='/game')
        app.register_blueprint(premium.premium_bp, url_prefix='/premium')
        
        db.create_all()  # Creates all the tables based on the models

    return app