CREATE TABLE levels (
    level_id SERIAL PRIMARY KEY,
    level_number INT NOT NULL UNIQUE,
    experience_required INT NOT NULL,
    reward JSONB DEFAULT '{}'
);