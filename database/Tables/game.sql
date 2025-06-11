-- Table: game_progress
-- Purpose: Tracks the progress of users in the game, including levels completed and timestamps.

CREATE TABLE game_progress (
    progress_id SERIAL PRIMARY KEY, -- Unique identifier for each progress record
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE, -- Links to the user in the 'users' table
    level_number INT NOT NULL CHECK (level_number > 0), -- Positive level number
    completed_at TIMESTAMP DEFAULT NOW() -- Timestamp when the level was completed
);

-- Index to improve query performance when filtering by user_id
CREATE INDEX idx_game_progress_user_id ON game_progress(user_id);
