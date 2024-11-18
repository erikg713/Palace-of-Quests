from app import db
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash

# User Model
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    wallet_address = db.Column(db.String(100), nullable=False)

    # Relationship to Avatar
    avatar = db.relationship('Avatar', backref='user', uselist=False)
    
    # Relationship to Quests
    quests = db.relationship('Quest', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "wallet_address": self.wallet_address
        }

# Avatar Model
class Avatar(db.Model):
    __tablename__ = 'avatars'
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.Integer, default=1)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    # Relationship to Items
    items = db.relationship('Item', backref='avatar', lazy=True)
    
    # Relationship to Quests
    quests = db.relationship('Quest', backref='avatar', lazy=True)

# Quest Model
class Quest(db.Model):
    __tablename__ = 'quests'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    difficulty = db.Column(db.Integer, nullable=False)
    is_completed = db.Column(db.Boolean, default=False)
    reward_points = db.Column(db.Integer)
    
    # Foreign key relationship to User
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # Foreign key relationship to Avatar
    avatar_id = db.Column(db.Integer, db.ForeignKey('avatars.id'))

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "difficulty": self.difficulty,
            "is_completed": self.is_completed,
            "reward_points": self.reward_points,
            "user_id": self.user_id,
            "avatar_id": self.avatar_id
        }

# Item Model
class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    equipped = db.Column(db.Boolean, default=False)

    # Foreign key relationship to Avatar
    avatar_id = db.Column(db.Integer, db.ForeignKey('avatars.id'))

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "equipped": self.equipped,
            "avatar_id": self.avatar_id
        }

# Payment Model
class Payment(db.Model):
    __tablename__ = 'payments'
    id = db.Column(db.Integer, primary_key=True)
    payment_id = db.Column(db.String(100), unique=True, nullable=False)
    status = db.Column(db.String(50), nullable=False, default="pending")
    txid = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "payment_id": self.payment_id,
            "status": self.status,
            "txid": self.txid,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

# PremiumBenefit Model
class PremiumBenefit(db.Model):
    __tablename__ = 'premium_benefits'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    price_pi = db.Column(db.Float, nullable=False)  # Price in Pi coins
    benefit_type = db.Column(db.String(50), nullable=False)  # e.g., xp_boost, item, guild_access
    duration_days = db.Column(db.Integer, default=30)  # For timed benefits

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price_pi": self.price_pi,
            "benefit_type": self.benefit_type,
            "duration_days": self.duration_days
        }

# LevelReward Model
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

# Apply Premium Benefit Logic
def apply_premium_benefit(user_id, benefit_id):
    benefit = PremiumBenefit.query.get(benefit_id)
    user = User.query.get(user_id)

    if benefit.benefit_type == "xp_boost":
        user.xp_boost_expires = datetime.utcnow() + timedelta(days=benefit.duration_days)
    elif benefit.benefit_type == "item":
        item = Item(name=benefit.name, description=benefit.description)
        user.avatar.items.append(item)
    elif benefit.benefit_type == "guild_access":
        user.guild_access_expires = datetime.utcnow() + timedelta(days=benefit.duration_days)

    db.session.commit()