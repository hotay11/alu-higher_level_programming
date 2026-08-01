-- lists all cities contained in hbtn_0d_usa, with the state name
-- the database name is passed as an argument of the mysql command
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
