# PostgreSQL Transactions and Error Handling

Transactions are fundamental database concepts that ensure data integrity and consistency by grouping operations that must succeed or fail as a unit.

## ACID Properties

PostgreSQL transactions follow ACID properties:

- **Atomicity**: All operations complete successfully or none do
- **Consistency**: Database remains in a valid state before and after transaction
- **Isolation**: Transactions operate independently of one another
- **Durability**: Once committed, changes persist even after system failures

## Basic Transaction Control

```sql
-- Start a transaction
BEGIN;

-- Perform operations
INSERT INTO accounts (user_id, balance) VALUES (1, 1000);
UPDATE accounts SET balance = balance - 500 WHERE user_id = 1;
INSERT INTO transactions (user_id, amount, type) VALUES (1, 500, 'withdrawal');

-- Commit changes
COMMIT;

-- Alternatively, roll back changes
-- ROLLBACK;
```

## Savepoints

Savepoints allow partial rollbacks within a transaction.

```sql
BEGIN;

INSERT INTO users (name) VALUES ('Alice');
SAVEPOINT user_added;

INSERT INTO accounts (user_id, balance) VALUES (LASTVAL(), 1000);
-- Oh no, we made a mistake!

-- Rollback to the savepoint
ROLLBACK TO user_added;

-- Try again
INSERT INTO accounts (user_id, balance) VALUES (LASTVAL(), 2000);

COMMIT;
```

## Transaction Isolation Levels

PostgreSQL supports different isolation levels to control how transactions interact:

1. **READ UNCOMMITTED**: Can read uncommitted changes (PostgreSQL treats this as READ COMMITTED)
2. **READ COMMITTED**: Can only read committed changes (default)
3. **REPEATABLE READ**: Same query returns same results throughout transaction
4. **SERIALIZABLE**: Full isolation, transactions behave as if executed serially

```sql
-- Set isolation level for a transaction
BEGIN ISOLATION LEVEL SERIALIZABLE;
-- Operations...
COMMIT;

-- Or set for session
SET SESSION CHARACTERISTICS AS TRANSACTION ISOLATION LEVEL REPEATABLE READ;
```

## Practice Exercise

1. Create a banking database with accounts and transactions tables
2. Implement a transfer function with transaction control
3. Test the following scenarios:
   - Successful transfer
   - Insufficient funds
   - Non-existent account
   - Concurrent transfers (simulate with multiple connections)
4. Implement proper error handling and reporting

In the next lecture, we'll explore advanced PostgreSQL features including views, stored procedures, and triggers.