sqlite3 catalog.db <<EOF
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL
);

INSERT INTO products (name, description, price) VALUES
    ('Laptop', 'A high-end laptop', 1200.00),
    ('Phone', 'Latest smartphone', 800.00);
EOF
