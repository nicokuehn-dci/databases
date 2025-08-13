# PostgreSQL Views, Functions, and Stored Procedures

This lecture covers PostgreSQL's capabilities for encapsulating and reusing logic through views, functions, and stored procedures.

## Views

Views are virtual tables representing the result of a stored query. They simplify complex queries and provide an additional security layer.

```sql
-- Simple view
CREATE VIEW active_customers AS
SELECT * FROM customers WHERE status = 'active';

-- Using the view
SELECT * FROM active_customers;
```

### Materialized Views

Unlike regular views, materialized views physically store the result set and need to be refreshed manually.

```sql
-- Create a materialized view
CREATE MATERIALIZED VIEW monthly_sales AS
SELECT 
    DATE_TRUNC('month', order_date) AS month,
    SUM(amount) AS total_sales
FROM orders
GROUP BY DATE_TRUNC('month', order_date)
ORDER BY month;
```

## Functions

Functions in PostgreSQL can return scalar values, sets of rows, or perform actions.

```sql
-- Simple function returning a scalar
CREATE OR REPLACE FUNCTION calculate_discount(price numeric, discount_percent numeric)
RETURNS numeric AS $$
BEGIN
    RETURN price * (1 - discount_percent / 100);
END;
$$ LANGUAGE plpgsql;

-- Using the function
SELECT calculate_discount(100, 15); -- Returns 85
```

### Table-Valued Functions

Functions can return complete result sets.

```sql
CREATE OR REPLACE FUNCTION get_customers_by_state(state_code text)
RETURNS TABLE(customer_id int, name text, city text) AS $$
BEGIN
    RETURN QUERY
    SELECT c.customer_id, c.name, c.city
    FROM customers c
    WHERE c.state = state_code;
END;
$$ LANGUAGE plpgsql;

-- Using the function
SELECT * FROM get_customers_by_state('CA');
```

## Stored Procedures

PostgreSQL 11+ supports stored procedures that can manage their own transactions.

```sql
CREATE OR REPLACE PROCEDURE transfer_funds(
    sender_id int,
    recipient_id int,
    amount numeric
)
AS $$
BEGIN
    -- Start transaction automatically
    UPDATE accounts 
    SET balance = balance - amount 
    WHERE user_id = sender_id;
    
    UPDATE accounts 
    SET balance = balance + amount 
    WHERE user_id = recipient_id;
    
    COMMIT;
EXCEPTION
    WHEN OTHERS THEN
        ROLLBACK;
        RAISE;
END;
$$ LANGUAGE plpgsql;

-- Call the procedure
CALL transfer_funds(101, 202, 500);
```

## Triggers

Triggers automatically execute functions when specified events occur.

```sql
-- Create a function for the trigger
CREATE OR REPLACE FUNCTION log_customer_changes()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO customer_audit(customer_id, changed_at, operation, changed_by)
    VALUES (NEW.customer_id, NOW(), TG_OP, current_user);
    
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create a trigger that uses this function
CREATE TRIGGER customer_changes
AFTER INSERT OR UPDATE
ON customers
FOR EACH ROW
EXECUTE FUNCTION log_customer_changes();
```

## Practice Exercises

1. Create a view that joins multiple tables to create a comprehensive report
2. Create a materialized view for an expensive aggregation query and set up a refresh schedule
3. Write a function that calculates prices including taxes and discounts
4. Create a stored procedure that handles a complex business process with error handling
5. Implement an audit trail using triggers to track all changes to important tables

In the next lecture, we'll explore PostgreSQL performance tuning, indexing strategies, and query optimization.