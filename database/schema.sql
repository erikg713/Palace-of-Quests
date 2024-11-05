CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(128) NOT NULL,
    wallet_address VARCHAR(100)
);

CREATE TABLE inventory (
    id SERIAL PRIMARY KEY,
    item_name VARCHAR(100),
    item_type VARCHAR(50),
    price NUMERIC(10, 2),
    user_id INTEGER REFERENCES users(id)
);

CREATE TABLE quests (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    is_completed BOOLEAN DEFAULT FALSE,
    user_id INTEGER REFERENCES users(id)
);

CREATE INDEX idx_user_id ON users (id);

CREATE TABLE payments (
    id SERIAL PRIMARY KEY,
    payment_id VARCHAR(100) UNIQUE NOT NULL,
    status VARCHAR(50) NOT NULL,
    txid VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

from app import db
from datetime import datetime

def update_payment_status(payment_id, status, txid=None):
    payment = Payment.query.filter_by(payment_id=payment_id).first()
    if payment:
        payment.status = status
        payment.txid = txid
        payment.updated_at = datetime.utcnow()
        db.session.commit()

ALTER TABLE payments
ADD COLUMN status VARCHAR(50) DEFAULT 'pending';

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(128) NOT NULL,
    wallet_address VARCHAR(100) NOT NULL
);

CREATE TABLE inventory (
    id SERIAL PRIMARY KEY,
    item_name VARCHAR(100),
    item_type VARCHAR(50),
    price NUMERIC(10, 2),
    user_id INTEGER REFERENCES users(id)
);

CREATE TABLE quests (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    is_completed BOOLEAN DEFAULT FALSE,
    user_id INTEGER REFERENCES users(id)
);

CREATE TABLE payments (
    id SERIAL PRIMARY KEY,
    payment_id VARCHAR(100) UNIQUE NOT NULL,
    status VARCHAR(50) NOT NULL DEFAULT 'pending',
    txid VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP
);

CREATE INDEX idx_user_id ON users (id);
CREATE INDEX idx_payment_id ON payments (payment_id);

ALTER TABLE quests 
    ADD COLUMN type VARCHAR(50) DEFAULT 'standard';
