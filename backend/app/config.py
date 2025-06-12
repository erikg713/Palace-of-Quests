# app/config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    PI_API_KEY = os.getenv("PI_API_KEY")
    PI_SECRET_SEED = os.getenv("PI_SECRET_SEED")
    PI_ENV = os.getenv("PI_ENV", "TESTNET")  # or MAINNET

# In your app factory:
# app.config.from_object("app.config.Config")
