# PostgreSQL Commands Cheat Sheet (DBeaver Edition)

> DBeaver does not support psql meta-commands (like `\dt`), so use SQL statements and GUI features instead.

---

## 🔍 Data Querying
```sql
SELECT * FROM table_name;
SELECT column1, column2 FROM table_name WHERE condition;
```

## ➕ Insert Data
```sql
INSERT INTO table_name (column1, column2) VALUES (value1, value2);
```

## ✏️ Update Data
```sql
UPDATE table_name SET column1 = value1 WHERE condition;
```

## ❌ Delete Data
```sql
DELETE FROM table_name WHERE condition;
```

## 🏗️ Create Table
```sql
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype
);
```

## 🛠 Alter Table
```sql
ALTER TABLE table_name ADD COLUMN column datatype;
ALTER TABLE table_name DROP COLUMN column;
```

## 🗑 Drop Table
```sql
DROP TABLE table_name;
```

## 👤 List Users (Roles)
```sql
SELECT rolname FROM pg_roles;
SELECT * FROM pg_roles WHERE rolcanlogin = true; -- Only login-enabled roles
```

## 🗃 List All Databases
```sql
SELECT datname FROM pg_database;
```
*DBeaver GUI: Expand "Databases" in the server tree to view all databases.*

## 📋 List Tables
```sql
SELECT table_name FROM information_schema.tables WHERE table_schema='public';
```
*DBeaver GUI: Expand your database → "Tables" node.*

## 📝 Describe Table Structure
```sql
SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'your_table';
```

## 💾 Backup/Restore Database
- Use DBeaver’s GUI or shell commands:
```bash
pg_dump -U username -h hostname -F c -b -v -f /path/to/backup.sql dbname
```

## ⚡️ Create/Drop Index
```sql
CREATE INDEX index_name ON table_name (column);
DROP INDEX index_name;
```

## 🧩 Create/Drop/View Function
```sql
CREATE FUNCTION ...
DROP FUNCTION ...
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
ALTER TABLE table_name ADD CONSTRAINT ...;
ALTER TABLE table_name DROP CONSTRAINT ...;
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