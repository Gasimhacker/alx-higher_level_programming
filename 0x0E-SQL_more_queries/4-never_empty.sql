-- Create the table `id_not_null` with attributes:
-- id INT with the default value 1
-- name VARCHAR(256)
-- If the table `id_not_null` already exists, the script should not fail
CREATE TABLE IF NOT EXISTS id_not_null (
	id 	INT 		DEFAULT 1,
	name 	VARCHAR(256)
);
