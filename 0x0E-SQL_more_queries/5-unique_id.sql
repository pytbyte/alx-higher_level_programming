-- Create table `unique_id`
-- ID default value and unique.
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT UNIQUE DEFAULT 1,
    name VARCHAR(256) NOT NULL
);