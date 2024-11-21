CREATE TABLE subscriptions (
    subscription_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE,
    subscription_type VARCHAR(50) NOT NULL, -- Example: "Premium"
    start_date TIMESTAMP DEFAULT NOW(),
    end_date TIMESTAMP NOT NULL, -- 1 year from start_date
    amount_paid NUMERIC(10, 2) NOT NULL CHECK (amount_paid >= 0),
    payment_status VARCHAR(20) DEFAULT 'Pending'
);