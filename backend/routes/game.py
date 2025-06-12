def register_routes(app):
    from .game import game_bp
    # import other blueprints similarly
    # from .users import users_bp
    # from .quests import quests_bp
    # from .transactions import transactions_bp

    app.register_blueprint(game_bp, url_prefix='/api/game')
    # register other blueprints here as needed