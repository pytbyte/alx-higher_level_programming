-- Create table `unique_id`
-- ID default value and unique.
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256) NOT NULL
);