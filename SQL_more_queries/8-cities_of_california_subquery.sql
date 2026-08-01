-- lists all cities of California, using a subquery (no JOIN)
-- the database name is passed as an argument of the mysql command
SELECT id, name FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = "California")
ORDER BY id ASC;
