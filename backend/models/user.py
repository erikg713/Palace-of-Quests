from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    level = db.Column(db.Integer, default=1)
    experience = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<User {self.username}>'
from .database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)  # Store hashed passwords
    level = db.Column(db.Integer, default=1)
    experience = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<User {self.username}>'
