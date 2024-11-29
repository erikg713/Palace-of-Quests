CREATE TABLE challenges (
    id SERIAL PRIMARY KEY,
    challenge_name VARCHAR(100),
    description TEXT,
    xp_reward INT,
    coin_reward DECIMAL(10, 2),
    difficulty_level INT, -- 1-10 scale
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
