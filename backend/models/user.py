from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from .database import db

USERNAME_MAX_LENGTH = 80
EMAIL_MAX_LENGTH = 120
PASSWORD_HASH_LENGTH = 200

class User(db.Model):
    """
    User model for Palace-of-Quests.
    Stores authentication, profile, and progression data.
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(USERNAME_MAX_LENGTH), unique=True, nullable=False, index=True)
    email = db.Column(db.String(EMAIL_MAX_LENGTH), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(PASSWORD_HASH_LENGTH), nullable=False)
    level = db.Column(db.Integer, default=1, nullable=False)
    experience = db.Column(db.Integer, default=0, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}', level={self.level})>"

    def set_password(self, password: str) -> None:
        """Hashes and sets the user's password."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        """Checks the user's password against the hash."""
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def is_valid_email(email: str) -> bool:
        """Basic email validation."""
        import re
        return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

    def update_experience(self, amount: int) -> None:
        """Adds experience and increases level if threshold is reached."""
        if amount < 0:
            raise ValueError("Experience amount must be non-negative.")
        self.experience += amount
        # Example leveling logic (adjust as needed)
        exp_to_level = 100 * self.level
        while self.experience >= exp_to_level:
            self.experience -= exp_to_level
            self.level += 1
            exp_to_level = 100 * self.level
