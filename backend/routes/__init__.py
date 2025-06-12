# backend/routes/__init__.py

def register_routes(app):
    from .quests import quests_bp
    from .users import users_bp
    from .transactions import transactions_bp
    from .items import items_bp
    # Import other blueprints as you add them

    app.register_blueprint(quests_bp, url_prefix='/api/quests')
    app.register_blueprint(users_bp, url_prefix='/api/users')
    app.register_blueprint(transactions_bp, url_prefix='/api/transactions')
    app.register_blueprint(items_bp, url_prefix='/api/items')