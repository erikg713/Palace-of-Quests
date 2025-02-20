from flask import Blueprint, request, jsonify
from app.models.user import User
from app import db

user_bp = Blueprint('user', __name__)

@user_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    new_user = User(
        username=data['username'],
        email=data['email'],
        password=data['password']  # Hash this in production!
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201

@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    return jsonify({
        'id': user.id,
        'username': user.username,
        'level': user.level,
        'experience': user.experience,
    })
