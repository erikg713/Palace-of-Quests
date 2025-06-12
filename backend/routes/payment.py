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

# routes/payments.py
from flask import Blueprint, request, jsonify
import requests
import os
from database import db
from models.pi_payment import PiNetworkPayment

payments_bp = Blueprint('payments', __name__)

PI_API_KEY = os.getenv("PI_API_KEY")
PI_WALLET_SEED = os.getenv("PI_WALLET_SEED")
APP_WALLET_ADDRESS = os.getenv("PI_APP_WALLET")  # Your receiving wallet

@payments_bp.route('/pi/create-payment', methods=['POST'])
def create_pi_payment():
    data = request.json
    amount = data.get('amount')
    pi_username = data.get('pi_username')
    plan = data.get('plan')

    # Create payment request
    payment_payload = {
        "amount": amount,
        "memo": f"Subscription for {plan}",
        "metadata": {"user": pi_username, "plan": plan},
        "to_address": APP_WALLET_ADDRESS
    }

    headers = {
        "Authorization": f"Key {PI_API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post("https://api.minepi.com/v2/payments", json=payment_payload, headers=headers)
    
    if response.status_code == 201:
        payment_data = response.json()
        payment_id = payment_data['identifier']

        new_payment = PiNetworkPayment(
            payment_id=payment_id,
            pi_username=pi_username,
            amount=amount,
            subscription_plan=plan,
            status='pending'
        )
        db.session.add(new_payment)
        db.session.commit()

        return jsonify({"payment_id": payment_id, "status": "pending"})
    else:
        return jsonify({"error": "Failed to create Pi payment"}), 400