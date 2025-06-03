from .database import db

class Quest(db.Model):
    """
    Represents a quest in the Palace of Quests application.

    Attributes:
        id (int): Unique identifier for the quest.
        name (str): The name of the quest.
        description (str): Detailed description of the quest.
        reward_points (int): Points rewarded upon completion of the quest.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    reward_points = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<Quest id={self.id} name={self.name}>'

    def validate_reward_points(self):
        """
        Validates that reward points are non-negative.
        """
        if self.reward_points < 0:
            raise ValueError("Reward points cannot be negative.")
