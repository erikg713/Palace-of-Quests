from datetime import datetime
from app.extensions import db

class Warrior(db.Model):
    __tablename__ = 'warriors'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    level = db.Column(db.Integer, default=1, nullable=False)
    experience = db.Column(db.Integer, default=0, nullable=False)
    class_type = db.Column(db.String(20), nullable=False)
    health = db.Column(db.Integer, default=100, nullable=False)
    attack = db.Column(db.Integer, default=10, nullable=False)
    defense = db.Column(db.Integer, default=5, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    __table_args__ = (
        db.UniqueConstraint('user_id', 'name', name='uq_user_warrior_name'),
        db.CheckConstraint("class_type IN ('Warrior', 'Mage', 'Rogue', 'Healer')", name='chk_warrior_class_type'),
        db.CheckConstraint('level >= 1', name='chk_warrior_level'),
        db.CheckConstraint('experience >= 0', name='chk_warrior_experience'),
        db.CheckConstraint('health >= 0', name='chk_warrior_health'),
        db.CheckConstraint('attack >= 0', name='chk_warrior_attack'),
        db.CheckConstraint('defense >= 0', name='chk_warrior_defense'),
    )

    def __repr__(self):
        return f"<Warrior(id={self.id}, name='{self.name}', level={self.level}, class_type='{self.class_type}')>"