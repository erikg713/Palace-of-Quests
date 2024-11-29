from flask import Blueprint, request, jsonify
from .models import db, User, UserProgress

bp = Blueprint('api', __name__)

@bp.route('/create-user', methods=['POST'])
def create_user():
    data = request.json
    verified_uid = data.get('uid')  # UID from Pi Platform /me API
    username = data.get('username')
    email = data.get('email')

    if not verified_uid:
        return jsonify({'error': 'UID is required'}), 400

    user = User.query.filter_by(uid=verified_uid).first()
    if not user:
        user = User(uid=verified_uid, username=username, email=email)
        db.session.add(user)
    else:
        user.username = username or user.username
        user.email = email or user.email

    db.session.commit()
    return jsonify({'message': 'User record created or updated successfully', 'user_id': user.id}), 200

@bp.route('/update-progress', methods=['POST'])
def update_progress():
    data = request.json
    verified_uid = data.get('uid')  # UID from Pi Platform /me API
    level = data.get('level')
    experience_points = data.get('experience_points')

    user = User.query.filter_by(uid=verified_uid).first()
    if not user:
        return jsonify({'error': 'User not found'}), 404

    progress = UserProgress.query.filter_by(user_id=user.id).first()
    if not progress:
        progress = UserProgress(user_id=user.id, level=level, experience_points=experience_points)
        db.session.add(progress)
    else:
        progress.level = level or progress.level
        progress.experience_points = experience_points or progress.experience_points

    db.session.commit()
    return jsonify({'message': 'Progress updated successfully'}), 200
