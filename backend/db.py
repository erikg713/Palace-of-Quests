# Replace with real DB logic later
payments = {}

def store_payment(payment_id, data):
    payments[payment_id] = data

def update_payment(payment_id, txid):
    if payment_id in payments:
        payments[payment_id]['txid'] = txid

def get_payment(payment_id):
    return payments.get(payment_id)
