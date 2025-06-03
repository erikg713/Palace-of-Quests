from typing import Optional, Dict, Any
from sqlalchemy.orm import validates
from app import db

class LevelReward(db.Model):
    """
    Represents a reward for achieving a specific level in the game.

    Attributes:
        level (int): The level at which the reward is unlocked.
        reward_name (str): Name of the reward.
        reward_description (str): Description of the reward.
        stat_boost (int): Boost in stats provided by the reward.
        item_unlock (Optional[str]): Item unlocked by the reward.
        quest_difficulty (int): Difficulty level of the associated quest.
    """
    __tablename__ = 'level_rewards'

    level = db.Column(db.Integer, primary_key=True)
    reward_name = db.Column(db.String(100), nullable=False, index=True)
    reward_description = db.Column(db.String(255), nullable=False)
    stat_boost = db.Column(db.Integer, default=0)
    item_unlock = db.Column(db.String(100), nullable=True)
    quest_difficulty = db.Column(db.Integer, default=1, index=True)

    @validates('stat_boost', 'quest_difficulty')
    def validate_positive_values(self, key: str, value: int) -> int:
        if value is not None and value < 0:
            raise ValueError(f"{key} must be a non-negative integer.")
        return value

    def to_dict(self) -> Dict[str, Any]:
        """
        Serialize the LevelReward instance to a dictionary.
        """
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

    def __repr__(self) -> str:
        return (
            f"<LevelReward(level={self.level}, "
            f"reward_name='{self.reward_name}', "
            f"stat_boost={self.stat_boost}, "
            f"item_unlock='{self.item_unlock}', "
            f"quest_difficulty={self.quest_difficulty})>"
        )
