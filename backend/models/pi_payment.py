from database import db
from datetime import datetime

class PiNetworkPayment(db.Model):
    __tablename__ = 'pi_network_payments'

    id = db.Column(db.Integer, primary_key=True)
    payment_id = db.Column(db.String, unique=True, nullable=False)
    pi_username = db.Column(db.String, nullable=False)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    subscription_plan = db.Column(db.String, nullable=False)
    status = db.Column(db.String, default='pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
