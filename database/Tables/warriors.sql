CREATE TABLE IF NOT EXISTS warriors (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    name VARCHAR(50) NOT NULL,
    level INTEGER NOT NULL DEFAULT 1 CHECK (level >= 1),
    experience INTEGER NOT NULL DEFAULT 0 CHECK (experience >= 0),
    class VARCHAR(20) NOT NULL CHECK (class IN ('Warrior', 'Mage', 'Rogue', 'Healer')),
    health INTEGER NOT NULL DEFAULT 100 CHECK (health >= 0),
    attack INTEGER NOT NULL DEFAULT 10 CHECK (attack >= 0),
    defense INTEGER NOT NULL DEFAULT 5 CHECK (defense >= 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(user_id, name)
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_warriors_user_id ON warriors(user_id);
CREATE INDEX IF NOT EXISTS idx_warriors_level ON warriors(level);

-- Trigger for updated_at
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
   NEW.updated_at = CURRENT_TIMESTAMP;
   RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS update_warrior_timestamp ON warriors;

CREATE TRIGGER update_warrior_timestamp
BEFORE UPDATE ON warriors
FOR EACH ROW
EXECUTE FUNCTION update_updated_at_column();