import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS

# Database and JWT initialization
db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    """Application factory for Palace of Quests backend API."""
    app = Flask(__name__)

    # Configuration (use environment variables for secrets and DB URI)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        'DATABASE_URL', 'postgresql://user:password@localhost/palace_of_quests'
    )
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'your_jwt_secret_key')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    jwt.init_app(app)
    CORS(app)

    # Register blueprints or routes here
    # Example: from .routes import register_routes; register_routes(app)
    # For now, include demonstration routes below

    quests = [
        {"id": 1, "name": "Defeat the Dragon", "reward": 500},
        {"id": 2, "name": "Find the Lost Artifact", "reward": 300},
    ]

    @app.route('/api/quests', methods=['GET'])
    def get_quests():
        """Fetch all quests (demo)."""
        return jsonify(quests), 200

    @app.route('/api/quests/<int:quest_id>', methods=['GET'])
    def get_quest(quest_id):
        """Fetch a specific quest by ID (demo)."""
        quest = next((q for q in quests if q['id'] == quest_id), None)
        if quest is None:
            return jsonify({"error": "Quest not found"}), 404
        return jsonify(quest), 200

    @app.route('/api/quests', methods=['POST'])
    def add_quest():
        """Add a new quest (demo)."""
        data = request.get_json()
        if not data or not all(k in data for k in ("name", "reward")):
            return jsonify({"error": "Invalid request: 'name' and 'reward' are required."}), 400

        new_id = max([q["id"] for q in quests], default=0) + 1
        new_quest = {
            "id": new_id,
            "name": data["name"],
            "reward": data["reward"]
        }
        quests.append(new_quest)
        return jsonify(new_quest), 201

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host="0.0.0.0")
