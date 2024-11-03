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
