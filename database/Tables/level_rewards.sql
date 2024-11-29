-- Drop the table if it already exists
DROP TABLE IF EXISTS level_rewards;

-- Create the table for level rewards
CREATE TABLE level_rewards (
    level_id INT PRIMARY KEY AUTO_INCREMENT,  -- Unique level identifier
    level_name VARCHAR(100) NOT NULL,         -- Name of the level
    reward_type VARCHAR(50) NOT NULL,         -- Type of reward (e.g., "Coins", "Item")
    reward_amount INT NOT NULL,               -- Quantity of the reward
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Insert initial data into level_rewards
INSERT INTO level_rewards (level_name, reward_type, reward_amount)
VALUES
    ('Level 1', 'Coins', 100),
    ('Level 2', 'Coins', 200),
    ('Level 3', 'Item', 1),
    ('Level 4', 'Coins', 500),
    ('Level 5', 'Bonus', 1);

-- Query to retrieve all rewards
SELECT * FROM level_rewards;

-- Query to get a specific level's reward
SELECT level_name, reward_type, reward_amount
FROM level_rewards
WHERE level_id = ?;  -- Replace '?' with the desired level_id
