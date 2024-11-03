from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from .config import Config

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    jwt.init_app(app)

    with app.app_context():
        from .routes import auth, marketplace, quests
        app.register_blueprint(auth.auth_bp, url_prefix='/auth')
        app.register_blueprint(marketplace.marketplace_bp, url_prefix='/marketplace')
        app.register_blueprint(quests.quests_bp, url_prefix='/quests')

        db.create_all()

    return app
