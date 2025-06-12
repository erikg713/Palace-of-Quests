CREATE TABLE properties (
    id SERIAL PRIMARY KEY, -- Unique identifier for each property
    property_name VARCHAR(100) NOT NULL UNIQUE, -- Name of the property
    description TEXT DEFAULT 'No description available', -- Description of the property
    base_price DECIMAL(10, 2) NOT NULL CHECK (base_price > 0), -- Base price must be greater than 0
    max_capacity INT NOT NULL DEFAULT 10 CHECK (max_capacity >= 1), -- Minimum capacity is 1
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP -- Timestamp of property creation
);

-- Add an index for faster lookups by property name
CREATE INDEX idx_property_name ON properties (property_name);
