CREATE TABLE skills (
    id SERIAL PRIMARY KEY,
    skill_name VARCHAR(100) NOT NULL,
    description TEXT,
    max_level INT DEFAULT 5, -- Maximum upgrade level
    base_cost DECIMAL(10, 2) NOT NULL, -- Cost for level 1
    xp_required INT NOT NULL, -- XP needed to unlock/upgrade
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
