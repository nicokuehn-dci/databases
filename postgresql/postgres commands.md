# PostgreSQL Commands Cheat Sheet (DBeaver Edition)

> DBeaver does not support psql meta-commands (like `\dt`), so use SQL statements and GUI features instead.

---

## 🔍 Data Querying
```sql
-- Basic SELECT
SELECT * FROM table_name;

-- SELECT with conditions
SELECT column1, column2 FROM table_name WHERE condition;

-- Example: Find all customers from Germany
SELECT customer_id, first_name, last_name, email 
FROM customers 
WHERE country = 'Germany';

-- Example: Find orders with total over $1000
SELECT order_id, customer_id, order_date, total_amount 
FROM orders 
WHERE total_amount > 1000.00
ORDER BY total_amount DESC;

-- Example: Count products by category
SELECT category_id, COUNT(*) as product_count 
FROM products 
GROUP BY category_id
HAVING COUNT(*) > 5;
```

## ➕ Insert Data
```sql
-- Basic insert
INSERT INTO table_name (column1, column2) VALUES (value1, value2);

-- Example: Add a new customer
INSERT INTO customers (first_name, last_name, email, phone, address)
VALUES ('John', 'Smith', 'john.smith@example.com', '+49123456789', 'Hauptstrasse 1, Berlin');

-- Example: Insert multiple records at once
INSERT INTO products (product_name, category_id, unit_price, in_stock)
VALUES 
    ('Laptop 15" Pro', 1, 1299.99, true),
    ('Wireless Mouse', 1, 29.99, true),
    ('USB-C Cable', 2, 12.50, true);

-- Example: Insert with a SELECT subquery
INSERT INTO premium_customers (customer_id, enrollment_date)
SELECT customer_id, CURRENT_DATE
FROM customers
WHERE total_purchases > 5000;
```

## ✏️ Update Data
```sql
-- Basic update
UPDATE table_name SET column1 = value1 WHERE condition;

-- Example: Update a customer's email address
UPDATE customers 
SET email = 'new.email@example.com' 
WHERE customer_id = 101;

-- Example: Update multiple columns
UPDATE products 
SET unit_price = unit_price * 1.10, last_updated = CURRENT_TIMESTAMP 
WHERE category_id = 3;

-- Example: Update with data from another table
UPDATE orders 
SET status = 'shipped', shipping_date = CURRENT_DATE 
WHERE order_id IN (SELECT order_id FROM shipping WHERE processed = true);

-- Example: Update all records in a table
UPDATE inventory SET last_checked = CURRENT_DATE;
```

## ❌ Delete Data
```sql
-- Basic delete
DELETE FROM table_name WHERE condition;

-- Example: Delete a specific customer
DELETE FROM customers WHERE customer_id = 101;

-- Example: Delete records matching multiple conditions
DELETE FROM orders 
WHERE order_date < '2023-01-01' AND status = 'delivered';

-- Example: Delete using a subquery
DELETE FROM products 
WHERE product_id IN (
    SELECT product_id 
    FROM inventory 
    WHERE stock_count = 0 AND discontinued = true
);

-- Example: Delete with a RETURNING clause to see deleted rows
DELETE FROM old_users 
WHERE last_login < '2022-01-01' 
RETURNING user_id, username, last_login;
```

## 🏗️ Create Table
```sql
-- Basic table creation
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype
);

-- Example: Create a customers table
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20),
    address TEXT,
    city VARCHAR(50),
    country VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Example: Create table with foreign key
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    order_date DATE DEFAULT CURRENT_DATE,
    total_amount NUMERIC(10,2),
    status VARCHAR(20) DEFAULT 'pending',
    CONSTRAINT fk_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
        ON DELETE RESTRICT
);

-- Example: Create table with check constraint
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    unit_price NUMERIC(10,2) CHECK (unit_price > 0),
    in_stock BOOLEAN DEFAULT true,
    category_id INTEGER
);
```

## 🛠 Alter Table
```sql
-- Basic alter commands
ALTER TABLE table_name ADD COLUMN column datatype;
ALTER TABLE table_name DROP COLUMN column;

-- Example: Add a new column to customers
ALTER TABLE customers ADD COLUMN birth_date DATE;

-- Example: Add a column with constraints
ALTER TABLE products ADD COLUMN weight NUMERIC(5,2) CHECK (weight > 0);

-- Example: Modify column data type
ALTER TABLE orders ALTER COLUMN status TYPE VARCHAR(50);

-- Example: Add a default value to an existing column
ALTER TABLE customers ALTER COLUMN active SET DEFAULT true;

-- Example: Add a primary key constraint
ALTER TABLE temporary_users ADD PRIMARY KEY (user_id);

-- Example: Add a foreign key constraint
ALTER TABLE order_details 
ADD CONSTRAINT fk_product 
FOREIGN KEY (product_id) 
REFERENCES products (product_id);

-- Example: Remove a constraint
ALTER TABLE products DROP CONSTRAINT products_weight_check;

-- Example: Rename a table
ALTER TABLE old_customers RENAME TO archived_customers;

-- Example: Rename a column
ALTER TABLE customers RENAME COLUMN phone TO contact_number;
```

## 🗑 Drop Table
```sql
-- Basic drop
DROP TABLE table_name;

-- Example: Drop a table if it exists
DROP TABLE IF EXISTS old_customers;

-- Example: Drop a table and cascade dependencies
DROP TABLE products CASCADE;

-- Example: Drop multiple tables
DROP TABLE temp_orders, temp_customers, temp_products;

-- Example: Drop with RESTRICT option (default behavior)
DROP TABLE categories RESTRICT;  -- Will fail if other objects depend on it
```

## 👤 List Users (Roles)
```sql
-- Basic role listing
SELECT rolname FROM pg_roles;

-- List only login-enabled roles
SELECT * FROM pg_roles WHERE rolcanlogin = true;

-- Example: List roles with details
SELECT rolname, rolsuper, rolcreaterole, rolcreatedb 
FROM pg_roles 
ORDER BY rolname;

-- Example: Find roles with specific permissions
SELECT rolname, rolcreatedb 
FROM pg_roles 
WHERE rolcreatedb = true;

-- Example: List role memberships
SELECT r.rolname AS role, m.rolname AS member
FROM pg_auth_members am
JOIN pg_roles r ON r.oid = am.roleid
JOIN pg_roles m ON m.oid = am.member
ORDER BY r.rolname, m.rolname;
```

## 🗃 List All Databases
```sql
-- Basic database listing
SELECT datname FROM pg_database;

-- Example: List databases with their sizes
SELECT pg_database.datname, 
       pg_size_pretty(pg_database_size(pg_database.datname)) AS size
FROM pg_database
ORDER BY pg_database_size(pg_database.datname) DESC;

-- Example: List databases with their owners
SELECT d.datname as "Database", 
       r.rolname as "Owner" 
FROM pg_database d
JOIN pg_roles r ON d.datdba = r.oid
WHERE d.datistemplate = false
ORDER BY d.datname;

-- Example: List databases with connection information
SELECT datname, datconnlimit
FROM pg_database
WHERE datallowconn = true;
```
*DBeaver GUI: Expand "Databases" in the server tree to view all databases.*

## 📋 List Tables
```sql
-- Basic table listing
SELECT table_name 
FROM information_schema.tables 
WHERE table_schema='public';

-- Example: List tables with their row counts
SELECT
    table_schema,
    table_name,
    (xpath('/row/cnt/text()', query_to_xml('SELECT count(*) AS cnt FROM '||quote_ident(table_schema)||'.'||quote_ident(table_name), true, false, '')))[1]::text::int AS row_count
FROM information_schema.tables
WHERE table_schema = 'public'
ORDER BY row_count DESC;

-- Example: List tables by size
SELECT
    table_name,
    pg_size_pretty(pg_total_relation_size(quote_ident(table_name))) AS total_size
FROM
    information_schema.tables
WHERE
    table_schema = 'public'
ORDER BY
    pg_total_relation_size(quote_ident(table_name)) DESC;

-- Example: List tables with their columns count
SELECT
    table_name,
    COUNT(column_name) AS columns_count
FROM
    information_schema.columns
WHERE
    table_schema = 'public'
GROUP BY
    table_name
ORDER BY
    columns_count DESC;
```
*DBeaver GUI: Expand your database → "Tables" node.*

## 📝 Describe Table Structure
```sql
-- Basic column information
SELECT column_name, data_type 
FROM information_schema.columns 
WHERE table_name = 'your_table';

-- Example: Get detailed column information for customers table
SELECT 
    column_name, 
    data_type, 
    character_maximum_length, 
    column_default, 
    is_nullable
FROM 
    information_schema.columns 
WHERE 
    table_name = 'customers' 
ORDER BY 
    ordinal_position;

-- Example: List primary key columns for a table
SELECT
    tc.constraint_name,
    kcu.column_name
FROM
    information_schema.table_constraints tc
JOIN
    information_schema.key_column_usage kcu
    ON tc.constraint_name = kcu.constraint_name
WHERE
    tc.constraint_type = 'PRIMARY KEY'
    AND tc.table_name = 'customers';

-- Example: List foreign key constraints
SELECT
    tc.constraint_name,
    kcu.column_name,
    ccu.table_name AS referenced_table,
    ccu.column_name AS referenced_column
FROM
    information_schema.table_constraints tc
JOIN
    information_schema.key_column_usage kcu
    ON tc.constraint_name = kcu.constraint_name
JOIN
    information_schema.constraint_column_usage ccu
    ON tc.constraint_name = ccu.constraint_name
WHERE
    tc.constraint_type = 'FOREIGN KEY'
    AND tc.table_name = 'orders';
```

## 💾 Backup/Restore Database
- Use DBeaver’s GUI or shell commands:
```bash
pg_dump -U username -h hostname -F c -b -v -f /path/to/backup.sql dbname
```

## ⚡️ Create/Drop Index
```sql
-- Basic index creation and deletion
CREATE INDEX index_name ON table_name (column);
DROP INDEX index_name;

-- Example: Create a B-tree index on a single column
CREATE INDEX idx_customers_email ON customers (email);

-- Example: Create a unique index
CREATE UNIQUE INDEX idx_products_code ON products (product_code);

-- Example: Create a multi-column index
CREATE INDEX idx_orders_customer_date ON orders (customer_id, order_date);

-- Example: Create a partial index
CREATE INDEX idx_active_users ON users (username) WHERE active = true;

-- Example: Create an index using an expression
CREATE INDEX idx_lower_last_name ON customers (LOWER(last_name));

-- Example: Create a GIN index (good for full-text search)
CREATE INDEX idx_product_description_gin ON products USING GIN (to_tsvector('english', description));

-- Example: Drop an index if it exists
DROP INDEX IF EXISTS idx_customers_email;

-- Example: Create an index concurrently (doesn't block writes)
CREATE INDEX CONCURRENTLY idx_orders_status ON orders (status);
```

## 🧩 Create/Drop/View Function
```sql
-- Example: Create a simple function to calculate total price
CREATE OR REPLACE FUNCTION calculate_total_price(
    price NUMERIC, 
    quantity INTEGER, 
    discount NUMERIC DEFAULT 0
)
RETURNS NUMERIC AS $$
BEGIN
    RETURN (price * quantity) * (1 - discount);
END;
$$ LANGUAGE plpgsql;

-- Example: Create a function that returns a table
CREATE OR REPLACE FUNCTION get_customers_by_country(country_name VARCHAR)
RETURNS TABLE (
    id INTEGER,
    full_name VARCHAR,
    email VARCHAR
) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        customer_id AS id,
        first_name || ' ' || last_name AS full_name,
        email
    FROM 
        customers
    WHERE 
        country = country_name
    ORDER BY 
        last_name, first_name;
END;
$$ LANGUAGE plpgsql;

-- Example: Using the function
SELECT * FROM get_customers_by_country('Germany');
SELECT calculate_total_price(19.99, 5, 0.1);

-- Example: Drop a function
DROP FUNCTION IF EXISTS calculate_total_price;
DROP FUNCTION IF EXISTS get_customers_by_country(VARCHAR);

-- Example: View function definition
SELECT pg_get_functiondef(oid) 
FROM pg_proc 
WHERE proname = 'calculate_total_price';
```
*DBeaver GUI: Expand "Functions" in the tree.*

## 🗂 Manage Schemas
```sql
CREATE SCHEMA schema_name;
DROP SCHEMA schema_name;
```
*Use DBeaver’s Schema GUI tools.*

## 🔒 Handle Constraints
```sql
-- Basic constraint syntax
ALTER TABLE table_name ADD CONSTRAINT ...;
ALTER TABLE table_name DROP CONSTRAINT ...;

-- Example: Add a primary key constraint
ALTER TABLE products 
ADD CONSTRAINT pk_products PRIMARY KEY (product_id);

-- Example: Add a unique constraint
ALTER TABLE users 
ADD CONSTRAINT unique_email UNIQUE (email);

-- Example: Add a foreign key constraint
ALTER TABLE orders 
ADD CONSTRAINT fk_orders_customer 
FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
ON DELETE RESTRICT ON UPDATE CASCADE;

-- Example: Add a check constraint
ALTER TABLE products 
ADD CONSTRAINT check_price_positive 
CHECK (price > 0);

-- Example: Add a not-null constraint
ALTER TABLE orders 
ALTER COLUMN order_date SET NOT NULL;

-- Example: Drop a constraint
ALTER TABLE products 
DROP CONSTRAINT check_price_positive;

-- Example: Disable/Enable a constraint
ALTER TABLE orders 
ALTER CONSTRAINT fk_orders_customer 
DEFERRABLE INITIALLY DEFERRED;

-- Example: List all constraints for a table
SELECT
    tc.constraint_name,
    tc.constraint_type,
    kcu.column_name
FROM
    information_schema.table_constraints tc
JOIN
    information_schema.key_column_usage kcu
    ON tc.constraint_name = kcu.constraint_name
WHERE
    tc.table_name = 'products'
ORDER BY
    tc.constraint_type;
```

---

## DBeaver-Specific GUI Actions
- **Data Import/Export:** Right-click tables/databases
- **Schema Compare:** Visual compare in GUI
- **Data Visualization:** Built-in chart, GIS, ERD features
- **Session/Lock Management:** Use "Session Manager" and "Lock Manager"

---

## ⚠️ Important Notes
- You cannot use psql meta-commands (`\dt`, `\du`, etc.) directly in DBeaver; use SQL queries or the GUI instead.
- Most admin and DDL commands for PostgreSQL work in DBeaver’s SQL Editor.
- For advanced tasks (event triggers, extensions, partitions), use SQL or DBeaver’s GUI.

---

This cheat sheet covers essential PostgreSQL commands and DBeaver features for fast, effective database management and learning.