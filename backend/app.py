from flask import Flask, request, jsonify
from pi_sdk_client import create_payment, submit_payment, complete_payment
from db import store_payment, update_payment, get_payment

app = Flask(__name__)

@app.route("/api/pi/create-payment", methods=["POST"])
def api_create_payment():
    data = request.json
    amount = data["amount"]
    memo = data["memo"]
    metadata = data["metadata"]
    uid = data["uid"]

    payment_id = create_payment(amount, memo, metadata, uid)
    store_payment(payment_id, {
        "uid": uid,
        "amount": amount,
        "memo": memo,
        "metadata": metadata
    })

    return jsonify({ "payment_id": payment_id })

@app.route("/api/pi/submit-payment", methods=["POST"])
def api_submit_payment():
    data = request.json
    payment_id = data["payment_id"]

    txid = submit_payment(payment_id)
    update_payment(payment_id, txid)

    return jsonify({ "txid": txid })

@app.route("/api/pi/complete-payment", methods=["POST"])
def api_complete_payment():
    data = request.json
    payment_id = data["payment_id"]
    txid = data["txid"]

    payment_obj = complete_payment(payment_id, txid)

    return jsonify({ "payment": payment_obj })

if __name__ == "__main__":
    app.run(debug=True)
