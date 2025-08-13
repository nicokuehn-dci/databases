# PostgreSQL Indexes and Constraints

This lecture covers two critical aspects of database design and optimization: indexes and constraints.

## Database Constraints

Constraints enforce rules on data in tables, ensuring data integrity and consistency.

### PRIMARY KEY Constraint

Uniquely identifies each row in a table.

```sql
-- As column constraint
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL
);

-- As table constraint
CREATE TABLE orders (
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    PRIMARY KEY (order_id, product_id)
);
```

## Indexes

Indexes improve query performance by allowing the database to find rows faster.

```sql
-- Simple index
CREATE INDEX idx_users_email ON users(email);

-- Multi-column index
CREATE INDEX idx_orders_date_status ON orders(order_date, status);
```