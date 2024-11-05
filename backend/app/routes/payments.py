from flask import Blueprint, request, jsonify
from app.utils.piAPI import approve_payment, complete_payment

payments_bp = Blueprint("payments", __name__)

@payments_bp.route("/approve", methods=["POST"])
def approve():
    payment_id = request.json.get("paymentId")
    try:
        result = approve_payment(payment_id)
        return jsonify({"message": f"Payment {payment_id} approved successfully"})
    except Exception as e:
        return jsonify({"error": "Approval failed"}), 500

@payments_bp.route("/complete", methods=["POST"])
def complete():
    payment_id = request.json.get("paymentId")
    txid = request.json.get("txid")
    try:
        result = complete_payment(payment_id, txid)
        return jsonify({"message": f"Payment {payment_id} completed successfully"})
    except Exception as e:
        return jsonify({"error": "Completion failed"}), 500

@payments_bp.route("/cancelled_payment", methods=["POST"])
def cancel_payment():
    payment_id = request.json.get("paymentId")
    # Handle custom logic for canceled payments if needed
    return jsonify({"message": f"Payment {payment_id} canceled"})

from flask import Blueprint, request, jsonify
from .utils import piAPI

payments_bp = Blueprint("payments", __name__)

@payments_bp.route("/approve", methods=["POST"])
def approve():
    payment_id = request.json.get("paymentId")
    try:
        piAPI.approve_payment(payment_id)
        return jsonify({"message": "Payment approved"})
    except Exception as e:
        return jsonify({"error": "Approval failed"}), 500

@payments_bp.route("/complete", methods=["POST"])
def complete():

@payments_bp.route("/approve", methods=["POST"])
def approve_payment():
    payment_id = request.json.get("paymentId")
    response = requests.post(
        f"https://api.minepi.com/v2/payments/{payment_id}/approve",
        headers={"Authorization": "Bearer YOUR_API_KEY"}
    )
    if response.status_code == 200:
        return jsonify({"message": f"Approved payment {payment_id}"})
    else:
        return jsonify({"error": "Approval failed"}), response.status_code
@payments_bp.route("/complete", methods=["POST"])
def complete_payment():
    payment_id = request.json.get("paymentId")
    txid = request.json.get("txid")
    response = requests.post(
        f"https://api.minepi.com/v2/payments/{payment_id}/complete",
        json={"txid": txid},
        headers={"Authorization": "Bearer YOUR_API_KEY"}
    )
    if response.status_code == 200:
        return jsonify({"message": f"Completed payment {payment_id}"})
    else:
        return jsonify({"error": "Completion failed"}), response.status_code
@payments_bp.route("/cancelled_payment", methods=["POST"])
def cancel_payment():
    payment_id = request.json.get("paymentId")
    # Custom cancellation handling logic here
    return jsonify({"message": f"Payment {payment_id} canceled"})

from flask import Blueprint, request, jsonify
from app.utils.piAPI import approve_payment, complete_payment

payments_bp = Blueprint("payments", __name__)

@payments_bp.route("/approve", methods=["POST"])
def approve():
    payment_id = request.json.get("paymentId")
    try:
        result = approve_payment(payment_id)
        return jsonify(result)
    except Exception as e:
        print(f"Error approving payment: {e}")
        return jsonify({"error": "Failed to approve payment"}), 500

@payments_bp.route("/complete", methods=["POST"])
def complete():
    payment_id = request.json.get("paymentId")
    txid = request.json.get("txid")
    try:
        result = complete_payment(payment_id, txid)
        return jsonify(result)
    except Exception as e:
        print(f"Error completing payment: {e}")
        return jsonify({"error": "Failed to complete payment"}), 500
