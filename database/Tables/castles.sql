-- Table: castles
-- Description: Stores information about castles in the Palace of Quests game.

CREATE TABLE IF NOT EXISTS castles (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    location VARCHAR(150),
    owner_id INTEGER REFERENCES users(id) ON DELETE SET NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE,
    defense_rating INTEGER DEFAULT 0 CHECK (defense_rating >= 0),
    magic_level INTEGER DEFAULT 0 CHECK (magic_level >= 0)
);

-- Index for faster search on castle name
CREATE INDEX IF NOT EXISTS idx_castles_name ON castles(name);

-- Trigger to update 'updated_at' timestamp on modification
CREATE OR REPLACE FUNCTION update_castles_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS trg_update_castles_updated_at ON castles;

CREATE TRIGGER trg_update_castles_updated_at
BEFORE UPDATE ON castles
FOR EACH ROW
EXECUTE FUNCTION update_castles_updated_at();

-- Optional: Seed with an example castle
INSERT INTO castles (name, description, location, defense_rating, magic_level)
VALUES
    ('Eternal Fortress', 'A legendary stronghold shrouded in mystery.', 'Northern Realm', 85, 60)
ON CONFLICT (name) DO NOTHING;
