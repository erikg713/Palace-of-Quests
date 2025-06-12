# app/models.py

from .import db
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.Text, nullable=False)
    wallet_address = db.Column(db.Text, unique=True)
    player_class = db.Column(db.String(20), nullable=False)  # Warrior, Mage, etc.
    level = db.Column(db.Integer, default=1)
    experience = db.Column(db.Integer, default=0)
    pi_balance = db.Column(db.Numeric(18,8), default=0)
    role = db.Column(db.String(20), default='player', nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class BattleZone(db.Model):
    __tablename__ = 'battle_zones'
    zone_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    difficulty = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Battle(db.Model):
    __tablename__ = 'battles'
    battle_id = db.Column(db.Integer, primary_key=True)
    zone_id = db.Column(db.Integer, db.ForeignKey('battle_zones.zone_id', ondelete='CASCADE'))
    name = db.Column(db.String(100), nullable=False)
    enemy_type = db.Column(db.String(50))
    enemy_power = db.Column(db.Integer)
    is_active = db.Column(db.Boolean, default=True)
    reward_hint = db.Column(db.Text)
    required_level = db.Column(db.Integer, default=1)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    zone = db.relationship('BattleZone', backref='battles')

class UserBattle(db.Model):
    __tablename__ = 'user_battles'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('users.id', ondelete='CASCADE'))
    battle_id = db.Column(db.Integer, db.ForeignKey('battles.battle_id', ondelete='CASCADE'))
    status = db.Column(db.String(20), default='in_progress')  # in_progress, victory, defeat
    started_at = db.Column(db.DateTime, default=datetime.utcnow)
    completed_at = db.Column(db.DateTime)

    user = db.relationship('User', backref='user_battles')
    battle = db.relationship('Battle', backref='user_battles')

class LevelReward(db.Model):
    __tablename__ = 'level_rewards'
    zone_id = db.Column(db.Integer, db.ForeignKey('battle_zones.zone_id', ondelete='CASCADE'), primary_key=True)
    zone_name = db.Column(db.String(100), unique=True, nullable=False)
    reward_type = db.Column(db.String(50), nullable=False)  # Coins, Item, Bonus, Gems, Relic
    reward_amount = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)