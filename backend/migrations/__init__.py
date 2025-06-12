def upgrade():
    op.execute("""
    CREATE TABLE IF NOT EXISTS level_rewards_audit_log (
        audit_id SERIAL PRIMARY KEY,
        zone_id INT NOT NULL REFERENCES battle_zones(zone_id) ON DELETE CASCADE,
        old_reward_amount INT,
        new_reward_amount INT,
        changed_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
    );
    """)

    op.execute("""
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
    """)

    op.execute("""
    CREATE TRIGGER trg_on_loot_update
    BEFORE UPDATE ON level_rewards
    FOR EACH ROW
    EXECUTE FUNCTION trg_update_loot();
    """)# Database migrations 
