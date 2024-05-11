-- Create the database
DROP TABLE IF EXISTS ingredient;

CREATE TABLE ingredient (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ingredient_id INTEGER NOT NULL,
    type TEXT NOT NULL,
    name TEXT NOT NULL,
    quantity REAL NOT NULL,
    in_date DATE NOT NULL,
    expiration_date DATE NOT NULL
);

INSERT INTO ingredient (ingredient_id, type, name, quantity, in_date, expiration_date) VALUES
(0, 'Sauce', 'Tomato sauce', 1, '2024-01-01', '2024-01-05'),
(0, 'Sauce', 'Tomato sauce', 1, '2024-01-01', '2024-01-05'),
(1, 'Vegetable', 'Onion', 0.2, '2024-01-01', '2024-01-05'),
(2, 'Vegetable', 'Carrot', 0.6, '2024-01-01', '2024-01-05'),
(3, 'Vegetable', 'Lettuce', 0.6, '2024-01-01', '2024-01-05');


