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
