# PostgreSQL `friends` Table Lesson in `psql`

*A practical exercise for learning basic PostgreSQL operations using the `friends` table*

---

## Prerequisites

- PostgreSQL installed and running
- Access to `psql` command-line tool
- A database named `company` (or create one with `CREATE DATABASE company;`)

---

## 1. Connect to Your Database

```sql
psql -U postgres -d company
```

**Alternative connection methods:**
```sql
-- Connect to specific host and port
psql -h localhost -p 5432 -U postgres -d company

-- Connect with password prompt
psql -U postgres -d company -W
```

---

## 2. View Table Structure

```sql
\d friends
```

**Expected output (if table exists):**
```
                                     Table "public.friends"
                                     
 Column |          Type          | Collation | Nullable |              Default
--------+------------------------+-----------+----------+------------------------------------
 id     | integer                |           | not null | nextval('friends_id_seq'::regclass)
 name   | character varying(100) |           |          |
 email  | character varying(255) |           |          |
 since  | date                   |           |          |
Indexes:
    "friends_pkey" PRIMARY KEY, btree (id)
```

---

## 3. Insert Data

### Insert One Entry

```sql
INSERT INTO friends (name, email, since)
VALUES ('Max Mustermann', 'max@email.com', '2022-09-01');
```

### Insert Multiple Entries at Once

```sql
INSERT INTO friends (name, email, since)
VALUES
  ('Sophie Schulz', 'sophie@email.com', '2023-01-15'),
  ('Lukas Klein', 'lukas@email.com', '2024-02-20'),
  ('Anna Weber', 'anna@email.com', '2023-06-10'),
  ('Tom Fischer', 'tom@email.com', '2024-01-05');
```

### Insert with NULL Values (Optional Fields)

```sql
INSERT INTO friends (name, email)
VALUES ('Unknown Friend', 'unknown@email.com');
-- 'since' will be NULL
```

---

## 4. Query Data

### View All Friends

```sql
SELECT * FROM friends;
```

### View Friends Since a Certain Date

```sql
SELECT * FROM friends
WHERE since >= '2023-01-01';
```

### Select Specific Columns

```sql
SELECT name, email FROM friends;
```

### Additional Query Examples

```sql
-- Order by name alphabetically
SELECT * FROM friends ORDER BY name;

-- Count total friends
SELECT COUNT(*) FROM friends;

-- Find friends with specific email domain
SELECT * FROM friends WHERE email LIKE '%@email.com';

-- Find friends added in 2023
SELECT * FROM friends 
WHERE since >= '2023-01-01' AND since < '2024-01-01';

-- Limit results
SELECT * FROM friends ORDER BY since DESC LIMIT 3;
```

---

## 5. Update Entries

### Change Email of a Friend

```sql
UPDATE friends
SET email = 'newemail@email.com'
WHERE id = 1;
```

### Update Multiple Fields

```sql
UPDATE friends
SET 
  name = 'Maximilian Mustermann',
  email = 'maximilian@email.com'
WHERE id = 1;
```

### Update Based on Condition

```sql
-- Update all friends with old email domain
UPDATE friends
SET email = REPLACE(email, '@email.com', '@newdomain.com')
WHERE email LIKE '%@email.com';
```

---

## 6. Delete Entries

### Remove Friend with Specific ID

```sql
DELETE FROM friends
WHERE id = 2;
```

### Delete Based on Condition

```sql
-- Remove friends added before 2023
DELETE FROM friends
WHERE since < '2023-01-01';
```

### ⚠️ **CAUTION: Delete All Records**

```sql
-- This will delete ALL friends - use with extreme caution!
-- DELETE FROM friends;
```

---

## 7. Useful Meta-Commands in psql

### Table and Database Information

```sql
-- List all tables in current database
\dt

-- List all databases
\l

-- Describe table structure
\d friends

-- Show table with indexes and constraints
\d+ friends

-- List all schemas
\dn
```

### Connection and System Info

```sql
-- Show current connection info
\conninfo

-- Show current database and user
\c

-- List all users/roles
\du

-- Show current working directory
\! pwd
```

### Query History and Help

```sql
-- Show command history
\s

-- Get help on SQL commands
\h SELECT

-- Get help on psql commands
\?

-- Quit psql
\q
```

---

## 8. Create `friends` Table (if needed)

```sql
CREATE TABLE friends (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  email VARCHAR(255) UNIQUE,
  since DATE DEFAULT CURRENT_DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Enhanced Table with Constraints

```sql
CREATE TABLE friends (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL CHECK (LENGTH(name) > 0),
  email VARCHAR(255) UNIQUE NOT NULL CHECK (email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'),
  since DATE DEFAULT CURRENT_DATE CHECK (since <= CURRENT_DATE),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 9. Practical Exercises

### Exercise 1: Basic Operations
1. Create the `friends` table
2. Insert 5 friends with different dates
3. Query all friends from 2024
4. Update one friend's email
5. Delete the oldest friend

### Exercise 2: Advanced Queries
```sql
-- Find friends added in the last 30 days
SELECT * FROM friends 
WHERE since >= CURRENT_DATE - INTERVAL '30 days';

-- Group friends by year they were added
SELECT EXTRACT(YEAR FROM since) AS year, COUNT(*) as friend_count
FROM friends 
GROUP BY EXTRACT(YEAR FROM since)
ORDER BY year;

-- Find friends with similar names (containing 'Max')
SELECT * FROM friends 
WHERE name ILIKE '%max%';
```

### Exercise 3: Data Validation
```sql
-- Check for duplicate emails
SELECT email, COUNT(*) 
FROM friends 
GROUP BY email 
HAVING COUNT(*) > 1;

-- Find friends without email
SELECT * FROM friends WHERE email IS NULL;

-- Validate email format (basic check)
SELECT * FROM friends 
WHERE email !~ '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$';
```

---

## 10. Running Commands from File

### Save commands to file
Create a file named `friends_exercise.sql`:

```sql
-- friends_exercise.sql
INSERT INTO friends (name, email, since) VALUES 
  ('Alice Johnson', 'alice@example.com', '2024-01-15'),
  ('Bob Smith', 'bob@example.com', '2024-02-20'),
  ('Carol Davis', 'carol@example.com', '2024-03-10');

SELECT 'Inserted friends:' AS message;
SELECT * FROM friends ORDER BY since;
```

### Run the file
```bash
psql -U postgres -d company -f friends_exercise.sql
```

### Alternative: Run commands and save output
```bash
psql -U postgres -d company -f friends_exercise.sql > output.txt
```

---

## 11. Backup and Restore

### Backup friends table
```bash
pg_dump -U postgres -d company -t friends > friends_backup.sql
```

### Restore from backup
```bash
psql -U postgres -d company < friends_backup.sql
```

---

## 12. Common Error Solutions

### Error: "relation 'friends' does not exist"
**Solution:** Create the table first using the CREATE TABLE command in section 8.

### Error: "duplicate key value violates unique constraint"
**Solution:** Check for existing email addresses before inserting.

### Error: "column 'id' cannot be null"
**Solution:** Don't specify id in INSERT (it's auto-generated) or use DEFAULT.

### Error: "permission denied"
**Solution:** Ensure you have proper database permissions or connect as superuser.

---

## Summary

This lesson covered:
- ✅ Connecting to PostgreSQL database
- ✅ Creating and examining table structure
- ✅ Inserting single and multiple records
- ✅ Querying data with various conditions
- ✅ Updating existing records
- ✅ Deleting records safely
- ✅ Using psql meta-commands
- ✅ Running SQL files
- ✅ Basic backup operations

**Next Steps:**
- Learn about JOINs with multiple tables
- Explore PostgreSQL functions and procedures
- Study indexing and performance optimization
- Practice with more complex queries

---

*This practical exercise provides hands-on experience with PostgreSQL fundamentals using a simple, relatable `friends` table structure.*
