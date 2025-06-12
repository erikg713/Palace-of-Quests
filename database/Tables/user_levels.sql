CREATE TABLE user_levels (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    level INTEGER NOT NULL DEFAULT 1 CHECK (level >= 1),
    experience INTEGER NOT NULL DEFAULT 0 CHECK (experience >= 0),
    reward_claimed BOOLEAN NOT NULL DEFAULT FALSE,
    pi_earned NUMERIC(18,8) DEFAULT 0.0 CHECK (pi_earned >= 0),
    last_level_up TIMESTAMP,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    UNIQUE(user_id)
);