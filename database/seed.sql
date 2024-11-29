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
-- Clear existing data and reset tables
DELETE FROM user_rewards;
DELETE FROM level_rewards;
DELETE FROM users;

-- Reset auto-increment counters
ALTER TABLE users AUTO_INCREMENT = 1;
ALTER TABLE level_rewards AUTO_INCREMENT = 1;
ALTER TABLE user_rewards AUTO_INCREMENT = 1;
-- Insert multiple users dynamically using a loop or random generator
INSERT INTO users (username, email, password, created_at)
SELECT 
    CONCAT('player', n) AS username,
    CONCAT('player', n, '@example.com') AS email,
    'password123' AS password,
    NOW() AS created_at
FROM (
    SELECT n FROM (SELECT 1 AS n UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4 UNION ALL SELECT 5) t
) numbers;

-- Check inserted users
SELECT * FROM users;
-- Insert rewards dynamically
INSERT INTO level_rewards (level_name, reward_type, reward_amount, created_at)
SELECT 
    CONCAT('Level ', n) AS level_name,
    CASE WHEN n % 3 = 0 THEN 'Item' 
         WHEN n % 5 = 0 THEN 'Gems' 
         ELSE 'Coins' 
    END AS reward_type,
    CASE WHEN n % 3 = 0 THEN 1 
         ELSE ROUND(RAND() * 500) + 50 
    END AS reward_amount,
    NOW() AS created_at
FROM (
    SELECT n FROM (SELECT 1 AS n UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4 UNION ALL SELECT 5 UNION ALL SELECT 6 UNION ALL SELECT 7 UNION ALL SELECT 8 UNION ALL SELECT 9 UNION ALL SELECT 10) t
) numbers;

-- Check inserted levels
SELECT * FROM level_rewards;
-- Assign random rewards to users
INSERT INTO user_rewards (user_id, level_id, claimed_at)
SELECT 
    u.id AS user_id,
    l.level_id AS level_id,
    CASE WHEN RAND() > 0.5 THEN NOW() ELSE NULL END AS claimed_at -- 50% chance of claiming
FROM users u
CROSS JOIN level_rewards l
WHERE RAND() > 0.7; -- Assign rewards to ~30% of possible combinations

-- Check inserted user rewards
SELECT * FROM user_rewards;
DELIMITER $$

CREATE PROCEDURE GenerateRewards(IN num_levels INT)
BEGIN
    DECLARE i INT DEFAULT 1;

    WHILE i <= num_levels DO
        INSERT INTO level_rewards (level_name, reward_type, reward_amount, created_at)
        VALUES (
            CONCAT('Level ', i),
            CASE 
                WHEN i % 3 = 0 THEN 'Item'
                WHEN i % 5 = 0 THEN 'Gems'
                ELSE 'Coins'
            END,
            CASE 
                WHEN i % 3 = 0 THEN 1
                ELSE ROUND(RAND() * 500) + 50
            END,
            NOW()
        );
        SET i = i + 1;
    END WHILE;
END$$

DELIMITER ;
CALL GenerateRewards(100); -- Generate 100 levels dynamically
SELECT * FROM level_rewards;
