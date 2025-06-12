from flask import Blueprint, request, jsonify
from services.game_service import GameService
from flask_jwt_extended import jwt_required, get_jwt_identity
import logging

# Define the blueprint
progress_bp = Blueprint('progress_bp', __name__)

@progress_bp.route('/update', methods=['POST'])
@jwt_required()
def update_progress():
    """
    Update the user's progress in the game.

    Returns:
        Response: JSON response with a success or error message.
    """
    try:
        # Get user ID from JWT token
        user_id = get_jwt_identity()
        
        # Parse and validate the request data
        data = request.get_json()
        if not data or 'progress' not in data:
            return jsonify({"error": "Invalid payload"}), 422
        
        progress = data['progress']
        
        # Validate progress (example: ensure it's a positive integer)
        if not isinstance(progress, int) or progress < 0:
            return jsonify({"error": "Invalid progress value"}), 422

        # Update progress using the service
        if GameService.update_user_progress(user_id, progress):
            logging.info(f"Progress updated successfully for user {user_id}")
            return jsonify({"message": "Progress updated"}), 200
        else:
            logging.warning(f"Failed to update progress for user {user_id}")
            return jsonify({"error": "Failed to update progress"}), 400

    except KeyError as e:
        logging.error(f"KeyError encountered: {e}")
        return jsonify({"error": "Malformed request"}), 400
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return jsonify({"error": "Internal server error"}), 500
