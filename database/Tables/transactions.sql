CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    transaction_type VARCHAR(50) NOT NULL, -- "purchase" or "subscription"
    item_id INT, -- For purchases
    amount DECIMAL(10, 2) NOT NULL, -- Amount in Pi coins
    transaction_id VARCHAR(255) UNIQUE, -- Blockchain transaction ID
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE,
    amount NUMERIC(10, 2) NOT NULL CHECK (amount >= 0),
    payment_method VARCHAR(50) NOT NULL, -- Example: "Pi Network"
    transaction_type VARCHAR(50) NOT NULL, -- Example: "Subscription", "Upgrade"
    status VARCHAR(20) DEFAULT 'Pending', -- Example: "Completed", "Failed"
    created_at TIMESTAMP DEFAULT NOW()
);