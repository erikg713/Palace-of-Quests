import jwt
from datetime import datetime, timedelta
from app.config import Config

def generate_jwt(payload, expires_in=3600):
    payload["exp"] = datetime.utcnow() + timedelta(seconds=expires_in)
    return jwt.encode(payload, Config.SECRET_KEY, algorithm="HS256")

def decode_jwt(token):
    try:
        return jwt.decode(token, Config.SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        return {"error": "Token expired"}
    except jwt.InvalidTokenError:
        return {"error": "Invalid token"}
