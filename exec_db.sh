sqlite3 catalog.db <<EOF

DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS users;

CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL,
    image TEXT
);

INSERT INTO products (name, description, price, image) VALUES
    ('Laptop', 'High-performance laptop with 16GB RAM', 1200.00, 'https://placehold.co/50x50'),
    ('Smartphone', 'Latest model with 128GB storage', 800.00, 'https://placehold.co/50x50'),
    ('Wireless Headphones', 'Noise-canceling over-ear headphones', 250.00, 'https://placehold.co/50x50'),
    ('Smartwatch', 'Fitness tracker with heart rate monitor', 150.00, 'https://placehold.co/50x50'),
    ('Gaming Console', 'Next-gen console with 1TB storage', 500.00, 'https://placehold.co/50x50'),
    ('Tablet', '10-inch display with stylus support', 300.00, 'https://placehold.co/50x50'),
    ('Bluetooth Speaker', 'Portable speaker with deep bass', 100.00, 'https://placehold.co/50x50'),
    ('Mechanical Keyboard', 'RGB backlit mechanical keyboard', 120.00, 'https://placehold.co/50x50'),
    ('External SSD', '1TB USB-C external solid-state drive', 180.00, 'https://placehold.co/50x50'),
    ('Drone', '4K camera drone with GPS and auto-pilot', 900.00, 'https://placehold.co/50x50');

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    status TEXT DEFAULT 'active'
);

EOF
