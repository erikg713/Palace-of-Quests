from flask import Blueprint, request, jsonify
from services.pi_payment_service import process_payment
from models.user_model import User

quest_blueprint = Blueprint('quests', __name__)

@quest_blueprint.route('/complete', methods=['POST'])
def complete_quest():
    data = request.get_json()
    user_id = data.get('user_id')
    payment_id = data.get('payment_id')
    try:
        user = User.query.filter_by(id=user_id).first()
        if not user:
            return jsonify({'error': 'User not found'}), 404

        # Process Pi token payment
        payment_result = process_payment(payment_id)
        return jsonify({'status': 'Quest completed', 'payment_result': payment_result}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

