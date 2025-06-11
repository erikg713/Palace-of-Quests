-- Create the table to store avatar information
CREATE TABLE avatars (
    id SERIAL PRIMARY KEY, -- Unique identifier for each avatar
    user_id INT NOT NULL,  -- Associate the avatar with a user
    avatar_url VARCHAR(255) NOT NULL, -- URL or path to the avatar image
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    CONSTRAINT fk_user FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Add an index to speed up queries on user_id
CREATE INDEX idx_user_id ON avatars (user_id);
