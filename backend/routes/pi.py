from flask import Blueprint, request, jsonify
from db.supabase_client import supabase
import requests
import os

pi_bp = Blueprint("pi", __name__)

# ENV variables for Pi Network API
PI_API_URL = "https://api.minepi.com/v2/"  # Use production URL as needed
PI_API_KEY = os.environ.get("PI_API_KEY")  # Set this in your env

def verify_pi_payment(payment_id, txid):
    """Verifies the payment with Pi Network's backend (mocked here)."""
    # In production, use Pi Network's backend API and verify with your server secret
    headers = {"Authorization": f"Key {PI_API_KEY}"}
    response = requests.get(f"{PI_API_URL}payments/{payment_id}", headers=headers)
    if response.status_code != 200:
        return False
    data = response.json()
    # Validate txid matches, status is completed, etc.
    return data.get("txid") == txid and data.get("status") == "completed"

@pi_bp.route("/create-payment", methods=["POST"])
def create_payment():
    data = request.get_json()
    required = {"payment_id", "uid", "amount", "memo", "metadata"}
    if not data or not required.issubset(data):
        return jsonify({"error": "Missing required fields"}), 400

    # Store the payment initiation in Supabase
    result = supabase.table("payments").insert({
        "payment_id": data["payment_id"],
        "uid": data["uid"],
        "amount": data["amount"],
        "memo": data["memo"],
        "metadata": data["metadata"],
        "status": "created"
    }).execute()
    if result.error:
        return jsonify({"error": "Database error"}), 500

    return jsonify({"payment_id": data["payment_id"]}), 201

@pi_bp.route("/submit-payment", methods=["POST"])
def submit_payment():
    data = request.get_json()
    payment_id = data.get("payment_id")
    txid = data.get("txid")
    if not payment_id or not txid:
        return jsonify({"error": "payment_id and txid required"}), 400

    # Verify payment with Pi Network
    if not verify_pi_payment(payment_id, txid):
        return jsonify({"error": "Payment verification failed"}), 400

    # Update payment status in Supabase
    result = supabase.table("payments").update({
        "txid": txid,
        "status": "submitted"
    }).eq("payment_id", payment_id).execute()
    if result.error:
        return jsonify({"error": "Database error"}), 500

    return jsonify({"txid": txid}), 200

@pi_bp.route("/complete-payment", methods=["POST"])
def complete_payment():
    data = request.get_json()
    payment_id = data.get("payment_id")
    txid = data.get("txid")
    if not payment_id or not txid:
        return jsonify({"error": "payment_id and txid required"}), 400

    # Final verification (optional, depending on your flow)
    if not verify_pi_payment(payment_id, txid):
        return jsonify({"error": "Payment verification failed"}), 400

    # Mark payment as completed in Supabase
    result = supabase.table("payments").update({
        "status": "completed"
    }).eq("payment_id", payment_id).execute()
    if result.error:
        return jsonify({"error": "Database error"}), 500

    return jsonify({"payment_id": payment_id, "status": "completed"}), 200

@pi_bp.route("/get-payment/<payment_id>", methods=["GET"])
def get_payment(payment_id):
    result = supabase.table("payments").select("*").eq("payment_id", payment_id).single().execute()
    if result.error or not result.data:
        return jsonify({"error": "Payment not found"}), 404
    return jsonify(result.data), 200
