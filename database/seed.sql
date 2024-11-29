-- Drop existing data and reset tables
DELETE FROM user_rewards;
DELETE FROM level_rewards;
DELETE FROM users;

-- Reset auto-increment counters
ALTER TABLE users AUTO_INCREMENT = 1;
ALTER TABLE level_rewards AUTO_INCREMENT = 1;
ALTER TABLE user_rewards AUTO_INCREMENT = 1;

-- Seed data for users
INSERT INTO users (username, email, password, created_at)
VALUES 
('player1', 'player1@example.com', 'password123', NOW()),
('player2', 'player2@example.com', 'password123', NOW()),
('player3', 'player3@example.com', 'password123', NOW());

-- Seed data for level_rewards
INSERT INTO level_rewards (level_name, reward_type, reward_amount, created_at)
VALUES
('Level 1', 'Coins', 100, NOW()),
('Level 2', 'Coins', 200, NOW()),
('Level 3', 'Item', 1, NOW()),
('Level 4', 'Gems', 50, NOW()),
('Level 5', 'Bonus', 1, NOW());

-- Seed data for user_rewards
INSERT INTO user_rewards (user_id, level_id, claimed_at)
VALUES
(1, 1, NOW()), -- Player 1 claimed Level 1 reward
(2, 1, NOW()), -- Player 2 claimed Level 1 reward
(2, 2, NULL),  -- Player 2 has not yet claimed Level 2 reward
(3, 3, NOW()); -- Player 3 claimed Level 3 reward

-- Optional: View seeded data
SELECT * FROM users;
SELECT * FROM level_rewards;
SELECT * FROM user_rewards;
