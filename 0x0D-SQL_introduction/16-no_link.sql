-- Display both the score and the name
-- List only rows that contains a name value
-- Records are ordered by score (top first)
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
