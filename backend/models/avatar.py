from sqlalchemy.orm import validates
from typing import List, Dict, Any
from . import db  # Assuming db is initialized elsewhere (like from flask_sqlalchemy import SQLAlchemy)

class Avatar(db.Model):
    """
    Represents an avatar in the Palace of Quests game.

    Attributes:
        id (int): Primary key for the avatar.
        user_id (int): Unique identifier for the associated user.
        level (int): Current level of the avatar.
        stat_points (int): Points available to allocate to stats.
        items (List[Item]): Collection of items owned by the avatar.
    """

    __tablename__ = 'avatars'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, unique=True, nullable=False, index=True)
    level = db.Column(db.Integer, default=1)
    stat_points = db.Column(db.Integer, default=0)

    items = db.relationship(
        'Item',
        backref='avatar',
        lazy='dynamic',
        cascade="all, delete-orphan"
    )

    @validates('level', 'stat_points')
    def validate_non_negative(self, key, value):
        if value is not None and value < 0:
            raise ValueError(f"{key} must be non-negative.")
        return value

    def to_dict(self, include_items: bool = False) -> Dict[str, Any]:
        data = {
            "id": self.id,
            "user_id": self.user_id,
            "level": self.level,
            "stat_points": self.stat_points
        }
        if include_items:
            # Assumes each Item has a to_dict() method
            data["items"] = [item.to_dict() for item in self.items.all()]
        return data

    def __repr__(self) -> str:
        return (f"<Avatar id={self.id} user_id={self.user_id} "
                f"level={self.level} stat_points={self.stat_points}>")
