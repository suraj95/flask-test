DROP TABLE IF EXISTS product;
DROP TABLE IF EXISTS location;
DROP TABLE IF EXISTS product_movement;

CREATE TABLE product (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE location (
    location_id INTEGER PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE product_movement (
    movement_id INTEGER PRIMARY KEY AUTOINCREMENT,
    movement_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    from_location INTEGER NULL,
    to_location INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NULL
);