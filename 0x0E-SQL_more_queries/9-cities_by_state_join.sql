-- List all cities contained in the database
-- Each record should display: cities.id - cities.name - states.name
SELECT c.id, c.name, s.name
  FROM states AS s
       INNER JOIN cities AS c
       ON c.state_id = s.id
 ORDER BY c.id
