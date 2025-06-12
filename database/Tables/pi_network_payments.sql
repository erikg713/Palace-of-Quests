CREATE TABLE IF NOT EXISTS pi_network_payments (
    id SERIAL PRIMARY KEY,
    payment_id TEXT UNIQUE NOT NULL,
    user_id INTEGER REFERENCES users(id),
    pi_username TEXT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    status TEXT CHECK (status IN ('pending', 'completed', 'cancelled')) NOT NULL,
    subscription_plan TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);