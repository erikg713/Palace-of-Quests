import os
import logging
from flask import Flask, request, jsonify
from pi_sdk_client import create_payment, submit_payment, complete_payment
from db import store_payment, update_payment, get_payment
from flask_cors import CORS

# Import your blueprints here
from routes.pi import pi_bp  # Example: adjust path as needed

# Import Supabase client (assume you have a module for this)
from db.supabase_client import supabase  # Example import
# Import your blueprints here
from your_blueprint_file import payments_bp  # Adjust the import as needed

def create_app():
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(payments_bp)

    # Payment API routes
    @app.route("/api/pi/create-payment", methods=["POST"])
    def api_create_payment():
        data = request.get_json()
        try:
            amount = data["amount"]
            memo = data["memo"]
            metadata = data["metadata"]
            uid = data["uid"]
        except (KeyError, TypeError):
            return jsonify({"error": "Missing or invalid fields"}), 400

        payment_id = create_payment(amount, memo, metadata, uid)
        store_payment(payment_id, {
            "uid": uid,
            "amount": amount,
            "memo": memo,
            "metadata": metadata
        })

        return jsonify({"payment_id": payment_id}), 201

    @app.route("/api/pi/submit-payment", methods=["POST"])
    def api_submit_payment():
        data = request.get_json()
        payment_id = data.get("payment_id")
        if not payment_id:
            return jsonify({"error": "payment_id is required"}), 400

        txid = submit_payment(payment_id)
        update_payment(payment_id, txid)

        return jsonify({"txid": txid}), 200

    @app.route("/api/pi/complete-payment", methods=["POST"])
    def api_complete_payment():
        data = request.get_json()
        payment_id = data.get("payment_id")
        txid = data.get("txid")

        if not payment_id or not txid:
            return jsonify({"error": "payment_id and txid are required"}), 400

        payment_obj = complete_payment(payment_id, txid)
        return jsonify({"payment": payment_obj}), 200

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
