-- List the number of records with the same score in the table second_table
-- The result will display the score and
-- the number of records for this score with the label number
SELECT score, count(score) AS 'number'
from second_table
GROUP BY score
ORDER BY `number` DESC;
