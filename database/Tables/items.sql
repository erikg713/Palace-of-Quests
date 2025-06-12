CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL UNIQUE, -- Ensure unique names
    description TEXT, -- Optional: Could be normalized if data is repetitive
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0), -- Price must be non-negative
    quantity INT DEFAULT 0 CHECK (quantity >= 0), -- Quantity must be non-negative
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, -- Track creation time
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Track last update time
);

-- Index for faster searches on name
CREATE INDEX idx_items_name ON items(name);

-- Comments for better documentation
COMMENT ON COLUMN items.id IS 'Primary key, unique identifier for each item';
COMMENT ON COLUMN items.name IS 'Name of the item, must be unique';
COMMENT ON COLUMN items.description IS 'Detailed description of the item';
COMMENT ON COLUMN items.price IS 'Price of the item, must be non-negative';
COMMENT ON COLUMN items.quantity IS 'Available quantity, must be non-negative';
COMMENT ON COLUMN items.created_at IS 'Timestamp when the item was created';
COMMENT ON COLUMN items.updated_at IS 'Timestamp when the item was last updated';
