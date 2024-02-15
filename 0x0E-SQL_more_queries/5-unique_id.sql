-- Create the table `unique_id` with attributes:
-- id INT with the default value 1 and must be unique
-- name VARCHAR(256)
-- If the table `unique_id` already exists, the script should not fail
CREATE TABLE IF NOT EXISTS unique_id (
	id	INT 		DEFAULT 1 	UNIQUE,
	name	VARCHAR(256)
);
