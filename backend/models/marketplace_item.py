from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy

db: SQLAlchemy = ...  # Should be initialized in your app context

class Item(db.Model):
    """
    Marketplace Item model representing purchasable items linked to avatars.
    """
    __tablename__ = 'items'

    id: int = Column(Integer, primary_key=True)
    name: str = Column(String(100), nullable=False)
    avatar_id: int = Column(Integer, ForeignKey('avatars.id'), nullable=False)

    # Optional: If you want to access related Avatar object
    avatar = relationship("Avatar", back_populates="items", lazy='joined')

    def __repr__(self) -> str:
        return f"<Item(id={self.id}, name='{self.name}', avatar_id={self.avatar_id})>"

    def to_dict(self, include_avatar: bool = False) -> dict:
        """
        Serializes the item to a dictionary.
        Args:
            include_avatar (bool): If True, includes related avatar info.
        Returns:
            dict: Serialized item.
        """
        data = {
            "id": self.id,
            "name": self.name,
            "avatar_id": self.avatar_id
        }
        if include_avatar and hasattr(self, "avatar") and self.avatar:
            data["avatar"] = self.avatar.to_dict() if hasattr(self.avatar, "to_dict") else str(self.avatar)
        return data
