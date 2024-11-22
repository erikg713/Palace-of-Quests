import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/pi_quest")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwt-secret-key")
# Configuration settings
import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://username:password@localhost/palace_of_quests")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PI_NETWORK_API_URL = "https://api.minepi.com"
    PI_NETWORK_SDK_KEY = os.getenv("PI_NETWORK_SDK_KEY")
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # Basic Flask configurations
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret')  # Default value for development
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///default.db')  # Fallback to SQLite for local testing
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable to save resources

    # JWT settings
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'default_jwt_secret')  # Separate secret for JWT
    JWT_ACCESS_TOKEN_EXPIRES = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES', 3600))  # Expiration time in seconds (default: 1 hour)

    # Security settings for cookies
    SESSION_COOKIE_SECURE = os.getenv('SESSION_COOKIE_SECURE', 'True') == 'True'  # Use secure cookies
    SESSION_COOKIE_HTTPONLY = os.getenv('SESSION_COOKIE_HTTPONLY', 'True') == 'True'  # Prevent client-side scripts from accessing cookies
    SESSION_COOKIE_SAMESITE = os.getenv('SESSION_COOKIE_SAMESITE', 'Lax')  # Options: 'Strict', 'Lax', 'None'

    # Caching (Optional)
    CACHE_TYPE = os.getenv('CACHE_TYPE', 'simple')  # Simple cache for development
    CACHE_DEFAULT_TIMEOUT = int(os.getenv('CACHE_DEFAULT_TIMEOUT', 300))  # Default cache timeout (in seconds)

    # Debugging
    DEBUG = os.getenv('FLASK_DEBUG', 'False') == 'True'  # Enable/disable debug mode dynamically