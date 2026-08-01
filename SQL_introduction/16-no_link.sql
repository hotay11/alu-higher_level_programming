-- lists all records of second_table that have a name value
-- results display score and name, ordered by descending score
-- the database name is passed as an argument of the mysql command
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
