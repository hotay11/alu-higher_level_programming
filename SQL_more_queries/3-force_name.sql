-- creates the table force_name
-- the database name is passed as an argument of the mysql command
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
