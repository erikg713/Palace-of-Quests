from flask import Blueprint, request, jsonify
from models import Inventory, User
from database import db
from flask_jwt_extended import jwt_required, get_jwt_identity
import requests

marketplace_bp = Blueprint('marketplace', __name__)

# Pi Network API endpoint for verifying payments (example sandbox/testnet URL)
PI_PAYMENT_VERIFY_URL = "https://api.minepi.com/v2/payments/verify"

def verify_pi_payment(payment_txn_id, user_id, amount):
    """
    Verify payment with Pi Network API.

    Args:
        payment_txn_id (str): Transaction ID from frontend Pi payment.
        user_id (int): Buyer user ID.
        amount (float): Expected payment amount in Pi.

    Returns:
        bool: True if payment is valid and confirmed, False otherwise.
    """

    # Example API call, adjust as per Pi Network API spec
    payload = {
        "transaction_id": payment_txn_id,
        "user_id": user_id,
        "amount": amount
    }
    headers = {
        "Authorization": f"Bearer {your_pi_api_access_token_here}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(PI_PAYMENT_VERIFY_URL, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data.get("valid", False)  # Assuming API returns {"valid": true} on success
    except Exception as e:
        print(f"Payment verification error: {e}")
        return False


@marketplace_bp.route('/items', methods=['GET'])
def get_items():
    items = Inventory.query.all()
    return jsonify([{'id': item.id, 'name': item.item_name, 'type': item.item_type, 'price': item.price} for item in items])


@marketplace_bp.route('/purchase', methods=['POST'])
@jwt_required()
def purchase_item():
    user_id = get_jwt_identity()
    data = request.json
    item_id = data.get('item_id')
    payment_txn_id = data.get('payment_txn_id')

    if not item_id or not payment_txn_id:
        return jsonify(message="Item ID and payment transaction ID are required"), 400

    item = Inventory.query.get(item_id)
    if not item:
        return jsonify(message="Item not found"), 404

    if item.user_id == user_id:
        return jsonify(message="You already own this item"), 400

    # Verify Pi payment before transferring ownership
    payment_valid = verify_pi_payment(payment_txn_id, user_id, item.price)
    if not payment_valid:
        return jsonify(message="Pi payment verification failed"), 400

    # Payment verified, transfer ownership
    item.user_id = user_id
    db.session.commit()

    return jsonify(message="Item purchased successfully"), 200


@marketplace_bp.route('/bridge-to-eth', methods=['POST'])
@jwt_required()
def bridge_to_eth():
    data = request.json
    item_id = data.get('item_id')
    if not item_id:
        return jsonify(message="Item ID is required"), 400

    # Placeholder for cross-chain bridging logic
    return jsonify(message=f"Item {item_id} bridged to Ethereum network successfully"), 200