# PostgreSQL Queries and Joins

This lecture covers how to query data from PostgreSQL databases, including filtering, sorting, and combining data from multiple tables using joins.

## Basic SELECT Statements

The SELECT statement retrieves data from one or more tables.

```sql
-- Basic select all columns
SELECT * FROM users;

-- Select specific columns
SELECT first_name, last_name, email FROM users;

-- Add a constant value in results
SELECT first_name, last_name, 'Active' AS status FROM users;

-- Use expressions
SELECT first_name, last_name, UPPER(email) AS email_uppercase FROM users;
```

## Filtering Data with WHERE

The WHERE clause filters records based on specified conditions.

```sql
-- Simple equality
SELECT * FROM products WHERE price = 19.99;

-- Comparison operators
SELECT * FROM products WHERE price > 100;

-- Multiple conditions with AND/OR
SELECT * FROM users 
WHERE (signup_date > '2023-01-01' AND country = 'Canada')
   OR (total_orders > 10);

-- Check for NULL values
SELECT * FROM users WHERE phone_number IS NULL;

-- LIKE for pattern matching
SELECT * FROM products WHERE name LIKE 'Apple%';

-- IN operator for multiple possible values
SELECT * FROM orders WHERE status IN ('Shipped', 'Delivered');

-- BETWEEN for range
SELECT * FROM products WHERE price BETWEEN 10 AND 20;
```

## Joins

Joins combine rows from multiple tables based on a related column.

### Types of Joins

1. **INNER JOIN**: Returns rows when there is a match in both tables
2. **LEFT JOIN**: Returns all rows from the left table and matched rows from the right table
3. **RIGHT JOIN**: Returns all rows from the right table and matched rows from the left table
4. **FULL JOIN**: Returns rows when there is a match in one of the tables

```sql
-- INNER JOIN
SELECT o.order_id, o.order_date, c.name, c.email
FROM orders o
INNER JOIN customers c ON o.customer_id = c.customer_id;

-- LEFT JOIN
SELECT c.name, c.email, o.order_id
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id;

-- Multiple joins
SELECT o.order_id, c.name, p.product_name, oi.quantity
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id;
```

## Practice Exercises

1. Create three related tables: `categories`, `products`, and `orders`
2. Insert sample data into each table
3. Write queries using different types of joins to relate data across tables
4. Use aggregation functions to calculate totals and averages
5. Create a query that uses filtering, sorting, joining, and aggregation

Next lecture will cover advanced PostgreSQL features including indexes, constraints, and transactions.