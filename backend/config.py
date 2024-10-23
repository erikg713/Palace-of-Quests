import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secure-secret-key')  # Ensure this is securely managed
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://user:password@localhost:5432/codequest_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'your-jwt-secret-key')
    JWT_ACCESS_TOKEN_EXPIRES = 3600  # Tokens expire after 1 hour
