-- Create the challenges table to store available challenges
CREATE TABLE challenges (
    challenge_id SERIAL PRIMARY KEY,
    challenge_name TEXT NOT NULL, -- Name of the challenge
    description TEXT, -- Detailed description of the challenge
    total_steps INT NOT NULL CHECK (total_steps > 0), -- Total steps required to complete the challenge
    reward DECIMAL(15, 2), -- Reward for completing the challenge
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Create the challenge_progress table to track user progress
CREATE TABLE challenge_progress (
    progress_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL, -- Reference to the user
    challenge_id INT NOT NULL, -- Reference to the challenge
    steps_completed INT DEFAULT 0 CHECK (steps_completed >= 0), -- Steps completed so far
    is_completed BOOLEAN DEFAULT FALSE, -- Whether the challenge is completed
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id), -- Maintain data integrity
    FOREIGN KEY (challenge_id) REFERENCES challenges(challenge_id)
);

-- Create indexes for performance optimization
CREATE INDEX idx_user_id ON challenge_progress(user_id);
CREATE INDEX idx_challenge_id ON challenge_progress(challenge_id);

-- Insert sample data into challenge_progress table
INSERT INTO challenge_progress (user_id, challenge_id, steps_completed, is_completed)
VALUES
    (1, 1, 20, FALSE), -- User 1 has completed 20 sword swings out of 100
    (2, 2, 50, TRUE);  -- User 2 has completed the shield mastery challenge
