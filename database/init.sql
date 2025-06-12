-- === SCHEMA CREATION ===
CREATE SCHEMA IF NOT EXISTS palace_of_quests_schema;
SET search_path TO palace_of_quests_schema;

-- === USERS TABLE (Warriors) ===
DROP TABLE IF EXISTS user_battles, battles, level_rewards_audit_log, level_rewards, battle_zones, users CASCADE;

CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    wallet_address TEXT UNIQUE,
    class VARCHAR(20) NOT NULL CHECK (class IN ('Warrior', 'Mage', 'Rogue', 'Archer')),
    level INT DEFAULT 1,
    experience INT DEFAULT 0,
    pi_balance NUMERIC(18,8) DEFAULT 0,
    role VARCHAR(20) NOT NULL DEFAULT 'player',
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- === BATTLE ZONES TABLE ===
CREATE TABLE battle_zones (
    zone_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    difficulty INT CHECK (difficulty BETWEEN 1 AND 10),
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- === BATTLES TABLE (Quests) ===
CREATE TABLE battles (
    battle_id SERIAL PRIMARY KEY,
    zone_id INT NOT NULL REFERENCES battle_zones(zone_id) ON DELETE CASCADE,
    name VARCHAR(100) NOT NULL,
    enemy_type VARCHAR(50),
    enemy_power INT,
    is_active BOOLEAN DEFAULT TRUE,
    reward_hint TEXT,
    required_level INT DEFAULT 1,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- === USER BATTLES TABLE (Progress) ===
CREATE TABLE user_battles (
    id SERIAL PRIMARY KEY,
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    battle_id INT NOT NULL REFERENCES battles(battle_id) ON DELETE CASCADE,
    status VARCHAR(20) NOT NULL CHECK (status IN ('in_progress', 'victory', 'defeat')) DEFAULT 'in_progress',
    started_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMPTZ
);

-- === LEVEL REWARDS TABLE (Loot) ===
CREATE TABLE level_rewards (
    zone_id INT PRIMARY KEY REFERENCES battle_zones(zone_id) ON DELETE CASCADE,
    zone_name VARCHAR(100) UNIQUE NOT NULL,
    reward_type VARCHAR(50) NOT NULL CHECK (reward_type IN ('Coins', 'Item', 'Bonus', 'Gems', 'Relic')),
    reward_amount INT NOT NULL CHECK (reward_amount > 0),
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- === AUDIT LOG (Loot Changes) ===
CREATE TABLE level_rewards_audit_log (
    audit_id SERIAL PRIMARY KEY,
    zone_id INT NOT NULL REFERENCES level_rewards(zone_id) ON DELETE CASCADE,
    old_reward_amount INT,
    new_reward_amount INT,
    changed_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- === TRIGGER FUNCTION (Audit + Timestamp) ===
CREATE OR REPLACE FUNCTION trg_update_loot()
RETURNS TRIGGER AS $$
BEGIN
    IF OLD.reward_amount IS DISTINCT FROM NEW.reward_amount THEN
        INSERT INTO level_rewards_audit_log(zone_id, old_reward_amount, new_reward_amount, changed_at)
        VALUES (OLD.zone_id, OLD.reward_amount, NEW.reward_amount, CURRENT_TIMESTAMP);
    END IF;
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- === TRIGGERS ===
CREATE TRIGGER trg_on_loot_update
BEFORE UPDATE ON level_rewards
FOR EACH ROW
EXECUTE FUNCTION trg_update_loot();

-- === INDEXES ===
CREATE INDEX idx_battles_active ON battles(is_active);
CREATE INDEX idx_user_battles_user_id ON user_battles(user_id);
CREATE INDEX idx_user_battles_status ON user_battles(status);
CREATE INDEX idx_rewards_type ON level_rewards(reward_type);

-- === ROLE & PERMISSIONS (App Access) ===
DO $$
BEGIN
    IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname = 'palace_app_user') THEN
        CREATE ROLE palace_app_user WITH LOGIN PASSWORD 'replace_this_securely';
    END IF;
END
$$;

GRANT USAGE ON SCHEMA palace_of_quests_schema TO palace_app_user;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA palace_of_quests_schema TO palace_app_user;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA palace_of_quests_schema TO palace_app_user;

ALTER DEFAULT PRIVILEGES IN SCHEMA palace_of_quests_schema
GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO palace_app_user;

ALTER DEFAULT PRIVILEGES IN SCHEMA palace_of_quests_schema
GRANT USAGE, SELECT ON SEQUENCES TO palace_app_user;

-- === SAMPLE DATA ===
INSERT INTO battle_zones (name, description, difficulty) VALUES
('Shadow Plains', 'A cursed battlefield haunted by fallen knights.', 2),
('Crystal Caves', 'Echoing caves filled with gem beasts.', 4),
('Inferno Keep', 'Lava-flooded castle ruled by fire demons.', 6);

INSERT INTO battles (zone_id, name, enemy_type, enemy_power, reward_hint, required_level) VALUES
(1, 'Skeleton Ambush', 'Undead Warrior', 12, '50 Coins', 1),
(2, 'Crystal Basilisk', 'Magical Beast', 34, 'Bonus', 3),
(3, 'Demon General', 'Fire Demon', 55, 'Relic', 5);

INSERT INTO level_rewards (zone_id, zone_name, reward_type, reward_amount) VALUES
(1, 'Shadow Plains', 'Coins', 50),
(2, 'Crystal Caves', 'Bonus', 100),
(3, 'Inferno Keep', 'Relic', 1);
