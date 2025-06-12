from flask import Blueprint, request, jsonify
from database import db
from models.pi_payment import PiNetworkPayment
import os, requests

payments_bp = Blueprint('payments', __name__, url_prefix='/api/payments')

# Load from environment variables
PI_API_KEY = os.getenv("PI_API_KEY")
APP_WALLET_ADDRESS = os.getenv("PI_APP_WALLET")

HEADERS = {
    "Authorization": f"Key {PI_API_KEY}",
    "Content-Type": "application/json"
}

# === Route: Create a new Pi Network Payment ===
@payments_bp.route('/create', methods=['POST'])
def create_payment():
    data = request.get_json()
    amount = data.get("amount")
    pi_username = data.get("pi_username")
    plan = data.get("plan")

    if not all([amount, pi_username, plan]):
        return jsonify({"error": "Missing required fields"}), 400

    payment_payload = {
        "amount": amount,
        "memo": f"Subscription for {plan}",
        "metadata": {"user": pi_username, "plan": plan},
        "to_address": APP_WALLET_ADDRESS
    }

    try:
        response = requests.post("https://api.minepi.com/v2/payments", json=payment_payload, headers=HEADERS)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Failed to create Pi payment: {str(e)}"}), 500

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

    return jsonify({"payment_id": payment_id, "status": "pending"}), 201


# === Route: Confirm a Pi Network Payment ===
@payments_bp.route('/complete', methods=['POST'])
def complete_payment():
    data = request.get_json()
    payment_id = data.get("payment_id")

    if not payment_id:
        return jsonify({"error": "Payment ID is required"}), 400

    try:
        response = requests.get(f"https://api.minepi.com/v2/payments/{payment_id}", headers=HEADERS)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Failed to verify Pi payment: {str(e)}"}), 500

    payment_data = response.json()
    status = payment_data.get("status")

    payment_record = PiNetworkPayment.query.filter_by(payment_id=payment_id).first()

    if not payment_record:
        return jsonify({"error": "Payment record not found"}), 404

    if status == "COMPLETED":
        payment_record.status = "completed"
        db.session.commit()
        return jsonify({"message": "Payment confirmed"}), 200
    else:
        return jsonify({"message": f"Payment not completed. Current status: {status}"}), 400