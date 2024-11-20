import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://username:password@localhost/palace_of_quests")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PI_NETWORK_API_URL = "https://api.minepi.com"
    PI_NETWORK_SDK_KEY = os.getenv("PI_NETWORK_SDK_KEY")