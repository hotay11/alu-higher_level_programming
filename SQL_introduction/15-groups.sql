-- lists the number of records with the same score in second_table
-- the database name is passed as an argument of the mysql command
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
