from .user_routes import user_bp

def register_routes(app):
    app.register_blueprint(user_bp, url_prefix='/api/users')
from flask import Blueprint

v1 = Blueprint('v1', __name__)
v2 = Blueprint('v2', __name__)

@v1.route('/quests', methods=['GET'])
def get_quests_v1():
    return {"message": "This is API v1"}

@v2.route('/quests', methods=['GET'])
def get_quests_v2():
    return {"message": "This is API v2 with enhanced features"}

def register_routes(app):
    app.register_blueprint(v1, url_prefix='/api/v1')
    app.register_blueprint(v2, url_prefix='/api/v2')
