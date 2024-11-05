from flask import Blueprint, request, jsonify
from app.models import Avatar, db

avatar_bp = Blueprint("avatar", __name__)

@avatar_bp.route("/customize_avatar", methods=["POST"])
def customize_avatar():
    data = request.get_json()
    attributes = data.get("attributes")
    avatar = Avatar.query.filter_by(user_id=1).first()  # Replace with actual user retrieval

    for attribute, value in attributes.items():
        setattr(avatar, attribute, value)

    db.session.commit()
    return jsonify(avatar.to_dict())
