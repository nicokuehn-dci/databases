# PostgreSQL Introduction

PostgreSQL is a powerful, open-source object-relational database system with over 30 years of active development. It has earned a strong reputation for reliability, feature robustness, and performance.

## Key Features

- **ACID Compliance**: Ensures reliability and data integrity
- **Extensible**: Create custom data types, functions, and languages
- **Multi-Version Concurrency Control (MVCC)**: Allows efficient handling of concurrent operations
- **Standards Compliant**: Implements a large part of the SQL standard
- **Open Source**: Free to use, modify, and distribute under PostgreSQL license
- **Wide Platform Support**: Runs on all major operating systems

## Installation

```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib

# Start service
sudo service postgresql start
```

## Basic Commands

```sql
-- Create a database
CREATE DATABASE mydatabase;

-- List all databases
\l

-- Connect to a database
\c mydatabase

-- Create a table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- List all tables
\dt

-- Describe a table
\d users
```

## Practice Exercise

1. Install PostgreSQL on your system
2. Create a new database called "practice_db"
3. Create a "students" table with columns: id, name, age, and enrollment_date
4. Insert at least 3 student records
5. Query all students and filter by age

This completes your introduction to PostgreSQL. In the next lecture, we'll explore PostgreSQL data types in detail.