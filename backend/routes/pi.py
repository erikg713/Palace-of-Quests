from flask import Blueprint, request, jsonify
from db.supabase_client import supabase

pi_bp = Blueprint('pi', __name__)

# Simulated Pi Network SDK functions -- replace with real SDK calls
def pi_sdk_create_payment(amount, memo, metadata, uid):
    # TODO: Replace with real Pi SDK integration
    return {"payment_id": f"pi_{uid}_{amount}", "status": "created"}

def pi_sdk_submit_payment(payment_id):
    # TODO: Replace with real Pi SDK call
    return {"txid": f"tx_{payment_id}", "status": "submitted"}

def pi_sdk_complete_payment(payment_id, txid):
    # TODO: Replace with real Pi SDK call
    return {"payment_id": payment_id, "txid": txid, "status": "completed"}

@pi_bp.route("/create-payment", methods=["POST"])
def create_payment():
    data = request.get_json()
    required = {"amount", "memo", "metadata", "uid"}
    if not data or not required.issubset(data):
        return jsonify({"error": "Missing required fields"}), 400

    # Pi SDK: Create payment
    pi_response = pi_sdk_create_payment(
        data["amount"], data["memo"], data["metadata"], data["uid"]
    )
    payment_id = pi_response["payment_id"]

    # Supabase: Store payment
    sb_result = supabase.table("payments").insert({
        "payment_id": payment_id,
        "uid": data["uid"],
        "amount": data["amount"],
        "memo": data["memo"],
        "metadata": data["metadata"],
        "status": "created"
    }).execute()
    if sb_result.error:
        return jsonify({"error": "Database error"}), 500
    return jsonify({"payment_id": payment_id}), 201

@pi_bp.route("/submit-payment", methods=["POST"])
def submit_payment():
    data = request.get_json()
    payment_id = data.get("payment_id")
    if not payment_id:
        return jsonify({"error": "payment_id required"}), 400

    pi_response = pi_sdk_submit_payment(payment_id)
    txid = pi_response["txid"]

    # Supabase: Update payment with txid and status
    sb_result = supabase.table("payments").update({
        "txid": txid,
        "status": "submitted"
    }).eq("payment_id", payment_id).execute()
    if sb_result.error:
        return jsonify({"error": "Database error"}), 500
    return jsonify({"txid": txid}), 200

@pi_bp.route("/complete-payment", methods=["POST"])
def complete_payment():
    data = request.get_json()
    payment_id = data.get("payment_id")
    txid = data.get("txid")
    if not payment_id or not txid:
        return jsonify({"error": "payment_id and txid required"}), 400

    pi_response = pi_sdk_complete_payment(payment_id, txid)

    # Supabase: Mark payment as completed
    sb_result = supabase.table("payments").update({
        "status": "completed"
    }).eq("payment_id", payment_id).execute()
    if sb_result.error:
        return jsonify({"error": "Database error"}), 500
    return jsonify({"payment": pi_response}), 200

@pi_bp.route("/get-payment/<payment_id>", methods=["GET"])
def get_payment(payment_id):
    sb_result = supabase.table("payments").select("*").eq("payment_id", payment_id).single().execute()
    if sb_result.error or not sb_result.data:
        return jsonify({"error": "Payment not found"}), 404
    return jsonify(sb_result.data), 200
