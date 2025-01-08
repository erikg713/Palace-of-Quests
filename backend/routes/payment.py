from flask import Blueprint, request, jsonify
from app.utils.pi_network_sdk import PiNetworkSDK

payments_bp = Blueprint('payments', __name__)
pi_sdk = PiNetworkSDK()

@payments_bp.route('/initiate', methods=['POST'])
def initiate_payment():
    data = request.get_json()
    user_id = data.get('user_id')
    amount = data.get('amount')
    metadata = data.get('metadata')  # Example: Quest ID, details, etc.

    if not user_id or not amount:
        return jsonify({"error": "User ID and amount are required"}), 400

    payment_identifier = pi_sdk.create_payment(user_id, amount, metadata)

    return jsonify({"payment_identifier": payment_identifier}), 200

@payments_bp.route('/complete', methods=['POST'])
def complete_payment():
    data = request.get_json()
    payment_identifier = data.get('payment_identifier')

    if not payment_identifier:
        return jsonify({"error": "Payment Identifier is required"}), 400

    payment_status = pi_sdk.verify_payment(payment_identifier)
    if payment_status.get("status") != "COMPLETED":
        return jsonify({"error": "Payment not completed"}), 400

    return jsonify({"message": "Payment confirmed"}), 200