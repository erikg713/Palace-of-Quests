import os
import requests
from dotenv import load_dotenv

load_dotenv()

PI_API_KEY = os.getenv("PI_API_KEY")
PI_WALLET_PRIVATE_SEED = os.getenv("PI_WALLET_PRIVATE_SEED")
BASE_URL = "https://api.minepi.com/v2"  # Replace if different

HEADERS = {
    "Authorization": f"Key {PI_API_KEY}",
    "Content-Type": "application/json"
}

def create_payment(amount, memo, metadata, uid):
    payload = {
        "amount": amount,
        "memo": memo,
        "metadata": metadata,
        "uid": uid
    }
    res = requests.post(f"{BASE_URL}/payments", headers=HEADERS, json=payload)
    res.raise_for_status()
    return res.json()["identifier"]

def submit_payment(payment_id):
    res = requests.post(f"{BASE_URL}/payments/{payment_id}/submit", headers=HEADERS)
    res.raise_for_status()
    return res.json()["txid"]

def complete_payment(payment_id, txid):
    payload = { "txid": txid }
    res = requests.post(f"{BASE_URL}/payments/{payment_id}/complete", headers=HEADERS, json=payload)
    res.raise_for_status()
    return res.json()["payment"]

def get_incomplete_payments():
    res = requests.get(f"{BASE_URL}/payments/incomplete", headers=HEADERS)
    res.raise_for_status()
    return res.json()["payments"]
