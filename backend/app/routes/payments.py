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
