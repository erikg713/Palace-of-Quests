# Marketplace items
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import MarketplaceItem, db

marketplace_bp = Blueprint('marketplace', __name__)

# Route to get all items in the marketplace
@marketplace_bp.route('/items', methods=['GET'])
def get_items():
    items = MarketplaceItem.query.all()
    return jsonify([item.to_dict() for item in items]), 200

# Route to add a new item to the marketplace
@marketplace_bp.route('/items', methods=['POST'])
@jwt_required()
def add_item():
    current_user = get_jwt_identity()
    data = request.json

    if not data or not all(k in data for k in ('name', 'description', 'price')):
        return jsonify({'error': 'Missing required fields'}), 400

    try:
        new_item = MarketplaceItem(
            name=data['name'],
            description=data['description'],
            price=float(data['price']),
            seller_id=current_user
        )
        db.session.add(new_item)
        db.session.commit()
        return jsonify({'message': 'Item added successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Route to update an item
@marketplace_bp.route('/items/<int:item_id>', methods=['PUT'])
@jwt_required()
def update_item(item_id):
    current_user = get_jwt_identity()
    data = request.json

    item = MarketplaceItem.query.get(item_id)

    if not item:
        return jsonify({'error': 'Item not found'}), 404
    if item.seller_id != current_user:
        return jsonify({'error': 'Unauthorized action'}), 403

    try:
        item.name = data.get('name', item.name)
        item.description = data.get('description', item.description)
        item.price = data.get('price', item.price)
        db.session.commit()
        return jsonify({'message': 'Item updated successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Route to delete an item
@marketplace_bp.route('/items/<int:item_id>', methods=['DELETE'])
@jwt_required()
def delete_item(item_id):
    current_user = get_jwt_identity()

    item = MarketplaceItem.query.get(item_id)

    if not item:
        return jsonify({'error': 'Item not found'}), 404
    if item.seller_id != current_user:
        return jsonify({'error': 'Unauthorized action'}), 403

    try:
        db.session.delete(item)
        db.session.commit()
        return jsonify({'message': 'Item deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
