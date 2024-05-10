-- Create the database
DROP TABLE IF EXISTS ingredient;

CREATE TABLE ingredient (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ingredient_id INTEGER NOT NULL UNIQUE,
    type TEXT NOT NULL,
    name TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    expiration_date DATE NOT NULL,
    in_date DATE NOT NULL
);


