from flask import Flask, jsonify
from flask_cors import CORS
from routes.pi import pi_bp

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(pi_bp, url_prefix="/api/pi")

    @app.route("/")
    def root():
        return jsonify({"msg": "Palace of Quests API"})

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=4000)
    # Register blueprints
    app.register_blueprint(pi_bp, url_prefix="/api/pi")

    @app.route("/")
    def root():
        return jsonify({"msg": "Palace of Quests API"})

    @app.route("/health")
    def health():
        return jsonify({"status": "ok"})

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0", port=4000)
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
