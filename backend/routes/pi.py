from flask import Blueprint, request, jsonify, current_app
from db.supabase_client import supabase
import requests
import logging
import os

pi_bp = Blueprint("pi", __name__)

# Set up logger for this module
logger = logging.getLogger(__name__)

# Securely load Pi Network API details from environment/config
PI_API_URL = os.environ.get("PI_API_URL", "https://api.minepi.com/v2/")
PI_API_KEY = os.environ.get("PI_API_KEY")  # Set securely in your environment

def get_pi_headers():
    if not PI_API_KEY:
        logger.error("PI_API_KEY not set in environment.")
        raise RuntimeError("Pi Network API key is not configured.")
    return {"Authorization": f"Key {PI_API_KEY}"}

def validate_fields(data, required_fields):
    missing = [field for field in required_fields if field not in data]
    if missing:
        logger.warning(f"Missing fields: {missing}")
        return False, missing
    return True, None

def pi_verify_payment(payment_id, txid):
    """Verify payment using Pi Network's backend API."""
    try:
        url = f"{PI_API_URL}payments/{payment_id}"
        headers = get_pi_headers()
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        payment = response.json()
        valid = payment.get("txid") == txid and payment.get("status") == "completed"
        logger.info(f"Pi payment verification for {payment_id}: {valid}")
        return valid
    except Exception as e:
        logger.error(f"Error verifying Pi payment: {e}")
        return False

@pi_bp.route("/create-payment", methods=["POST"])
def create_payment():
    data = request.get_json()
    required = {"payment_id", "uid", "amount", "memo", "metadata"}
    valid, missing = validate_fields(data, required)
    if not valid:
        return jsonify({"error": f"Missing required fields: {missing}"}), 400

    # Insert payment record into Supabase
    try:
        result = supabase.table("payments").insert({
            "payment_id": data["payment_id"],
            "uid": data["uid"],
            "amount": data["amount"],
            "memo": data["memo"],
            "metadata": data["metadata"],
            "status": "created"
        }).execute()
        if result.error:
            logger.error(f"Supabase insert error: {result.error}")
            return jsonify({"error": "Database error"}), 500
        logger.info(f"Payment created: {data['payment_id']}")
        return jsonify({"payment_id": data["payment_id"]}), 201
    except Exception as e:
        logger.error(f"Exception in create_payment: {e}")
        return jsonify({"error": "Internal server error"}), 500

@pi_bp.route("/submit-payment", methods=["POST"])
def submit_payment():
    data = request.get_json()
    required = {"payment_id", "txid"}
    valid, missing = validate_fields(data, required)
    if not valid:
        return jsonify({"error": f"Missing required fields: {missing}"}), 400

    payment_id = data["payment_id"]
    txid = data["txid"]

    # Verify payment with Pi Network
    if not pi_verify_payment(payment_id, txid):
        return jsonify({"error": "Payment verification failed"}), 400

    # Update payment record in Supabase
    try:
        result = supabase.table("payments").update({
            "txid": txid,
            "status": "submitted"
        }).eq("payment_id", payment_id).execute()
        if result.error:
            logger.error(f"Supabase update error: {result.error}")
            return jsonify({"error": "Database error"}), 500
        logger.info(f"Payment submitted: {payment_id}, txid: {txid}")
        return jsonify({"txid": txid}), 200
    except Exception as e:
        logger.error(f"Exception in submit_payment: {e}")
        return jsonify({"error": "Internal server error"}), 500

@pi_bp.route("/complete-payment", methods=["POST"])
def complete_payment():
    data = request.get_json()
    required = {"payment_id", "txid"}
    valid, missing = validate_fields(data, required)
    if not valid:
        return jsonify({"error": f"Missing required fields: {missing}"}), 400

    payment_id = data["payment_id"]
    txid = data["txid"]

    # Final verification (optional, but recommended)
    if not pi_verify_payment(payment_id, txid):
        return jsonify({"error": "Payment verification failed"}), 400

    # Mark payment as completed in Supabase
    try:
        result = supabase.table("payments").update({
            "status": "completed"
        }).eq("payment_id", payment_id).execute()
        if result.error:
            logger.error(f"Supabase update error: {result.error}")
            return jsonify({"error": "Database error"}), 500
        logger.info(f"Payment completed: {payment_id}")
        return jsonify({"payment_id": payment_id, "status": "completed"}), 200
    except Exception as e:
        logger.error(f"Exception in complete_payment: {e}")
        return jsonify({"error": "Internal server error"}), 500

@pi_bp.route("/get-payment/<payment_id>", methods=["GET"])
def get_payment(payment_id):
    try:
        result = supabase.table("payments").select("*").eq("payment_id", payment_id).single().execute()
        if result.error or not result.data:
            logger.warning(f"Payment not found: {payment_id}")
            return jsonify({"error": "Payment not found"}), 404
        logger.info(f"Payment retrieved: {payment_id}")
        return jsonify(result.data), 200
    except Exception as e:
        logger.error(f"Exception in get_payment: {e}")
        return jsonify({"error": "Internal server error"}), 500
