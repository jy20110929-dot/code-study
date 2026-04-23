CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    nutrients JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Example of inserting a master product
INSERT INTO products (id, name, description, nutrients)
VALUES 
(1, 'Master Product', 'This product serves as the reference for all nutrients.', '{}');