from flask import jsonify, request
from app.models import QuestProgress, db
from flask_jwt_extended import jwt_required, get_jwt_identity

@auth.route('/quests/progress', methods=['POST'])
@jwt_required()
def update_quest_progress():
    user_id = get_jwt_identity()
    data = request.get_json()

    quest_progress = QuestProgress.query.filter_by(user_id=user_id, quest_id=data['quest_id']).first()
    if not quest_progress:
        quest_progress = QuestProgress(user_id=user_id, quest_id=data['quest_id'])
        db.session.add(quest_progress)

    quest_progress.progress = data.get('progress', quest_progress.progress)
    quest_progress.completed = data.get('completed', quest_progress.completed)
    db.session.commit()

    return jsonify({"message": "Quest progress updated", "progress": quest_progress.progress}), 200
