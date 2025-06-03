from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from enum import Enum

db: SQLAlchemy = ...  # Should be initialized in your app context

class ItemType(Enum):
    WEAPON = "Weapon"
    ARMOR = "Armor"
    POTION = "Potion"

class Item(db.Model):
    """
    Marketplace Item model representing purchasable items linked to avatars.

    Attributes:
        id (int): Unique identifier for the item.
        name (str): Name of the item.
        avatar_id (int): Foreign key linking the item to an avatar.
        avatar (Avatar): The related Avatar object, if loaded.
    """
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    avatar_id = Column(Integer, ForeignKey('avatars.id'), nullable=False, index=True)

    # Optional: If you want to access related Avatar object
    avatar = relationship("Avatar", back_populates="items", lazy='select')

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
        if include_avatar:
            try:
                data["avatar"] = self.avatar.to_dict() if hasattr(self.avatar, "to_dict") else str(self.avatar)
            except AttributeError:
                data["avatar"] = None
        return data

    @classmethod
    def create(cls, name: str, avatar_id: int) -> "Item":
        """
        Factory method to create an Item instance.
        Args:
            name (str): Name of the item.
            avatar_id (int): ID of the related avatar.
        Returns:
            Item: The created item instance.
        """
        return cls(name=name.strip(), avatar_id=avatar_id)
