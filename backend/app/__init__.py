from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    jwt.init_app(app)

    # Register Blueprints
    from app.routes.auth import auth_bp
    from app.routes.player import player_bp
    from app.routes.challenges import challenges_bp
    from app.routes.marketplace import marketplace_bp
    from app.routes.payments import payments_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(player_bp)
    app.register_blueprint(challenges_bp)
    app.register_blueprint(marketplace_bp)
    app.register_blueprint(payments_bp)

    return app
