from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# In-memory data for demonstration purposes
quests = [
    {"id": 1, "name": "Defeat the Dragon", "reward": 500},
    {"id": 2, "name": "Find the Lost Artifact", "reward": 300},
]

@app.route('/api/quests', methods=['GET'])
def get_quests():
    """Fetch all quests."""
    return jsonify(quests)

@app.route('/api/quests/<int:quest_id>', methods=['GET'])
def get_quest(quest_id):
    """Fetch a specific quest by ID."""
    quest = next((q for q in quests if q['id'] == quest_id), None)
    if not quest:
        return jsonify({"error": "Quest not found"}), 404
    return jsonify(quest)

@app.route('/api/quests', methods=['POST'])
def add_quest():
    """Add a new quest."""
    data = request.json
    new_quest = {"id": len(quests) + 1, "name": data["name"], "reward": data["reward"]}
    quests.append(new_quest)
    return jsonify(new_quest), 201

if __name__ == '__main__':
    app.run(debug=True)

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost/palace_of_quests'
    app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    jwt.init_app(app)
    CORS(app)

    from app.routes import register_routes  # Import API routes dynamically
    register_routes(app)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
