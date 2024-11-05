from app import db

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    wallet_address = db.Column(db.String(100), nullable=False)
    
    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "wallet_address": self.wallet_address
        }

class LevelReward(db.Model):
    __tablename__ = 'level_rewards'
    level = db.Column(db.Integer, primary_key=True)
    reward_name = db.Column(db.String(100))
    reward_description = db.Column(db.Text)
    stat_boost = db.Column(db.Integer, default=0)
    item_unlock = db.Column(db.String(100))
    quest_difficulty = db.Column(db.Integer)

    def to_dict(self):
        return {
            "level": self.level,
            "reward_name": self.reward_name,
            "reward_description": self.reward_description,
            "stat_boost": self.stat_boost,
            "item_unlock": self.item_unlock,
            "quest_difficulty": self.quest_difficulty
        }
