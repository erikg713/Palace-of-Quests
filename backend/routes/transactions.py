from flask import Blueprint, request, jsonify
from decimal import Decimal
from app.extensions import db
from app.models.transaction import Transaction, TransactionType
from app.models.user import User
from app.core.exceptions import ValidationError, InsufficientFundsError

transactions_bp = Blueprint('transactions', __name__, url_prefix='/api/transactions')


@transactions_bp.route('/transfer', methods=['POST'])
def create_transfer():
    try:
        data = request.get_json()
        sender_id = data.get('sender_id')
        receiver_id = data.get('receiver_id')
        amount = Decimal(data.get('amount'))
        description = data.get('description')

        if not sender_id or not receiver_id or not amount:
            return jsonify({'error': 'Missing required fields'}), 400

        sender = User.query.get(sender_id)
        receiver = User.query.get(receiver_id)

        if not sender or not receiver:
            return jsonify({'error': 'Invalid sender or receiver ID'}), 404

        txn = Transaction.create_transfer(sender, receiver, amount, description)
        db.session.add(txn)
        db.session.commit()

        return jsonify({'transaction': txn.to_dict()}), 201

    except (ValidationError, InsufficientFundsError) as ve:
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Server error', 'details': str(e)}), 500


@transactions_bp.route('/<txn_id>/process', methods=['POST'])
def process_transaction(txn_id):
    txn = Transaction.query.get(txn_id)
    if not txn:
        return jsonify({'error': 'Transaction not found'}), 404

    try:
        success = txn.process()
        db.session.commit()
        return jsonify({'transaction': txn.to_dict(include_sensitive=True), 'success': success}), 200
    except ValidationError as ve:
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Processing failed', 'details': str(e)}), 500


@transactions_bp.route('/<txn_id>/refund', methods=['POST'])
def refund_transaction(txn_id):
    txn = Transaction.query.get(txn_id)
    if not txn:
        return jsonify({'error': 'Transaction not found'}), 404

    try:
        reason = request.json.get('reason', '')
        refund_txn = txn.refund(reason=reason)
        db.session.commit()
        return jsonify({'refund_transaction': refund_txn.to_dict()}), 201
    except ValidationError as ve:
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Refund failed', 'details': str(e)}), 500


@transactions_bp.route('/<txn_id>/cancel', methods=['POST'])
def cancel_transaction(txn_id):
    txn = Transaction.query.get(txn_id)
    if not txn:
        return jsonify({'error': 'Transaction not found'}), 404

    try:
        reason = request.json.get('reason', '')
        txn.cancel(reason)
        db.session.commit()
        return jsonify({'transaction': txn.to_dict()}), 200
    except ValidationError as ve:
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Cancellation failed', 'details': str(e)}), 500