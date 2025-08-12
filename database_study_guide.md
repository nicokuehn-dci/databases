# Database Study Guide

## 1. Introduction to Databases
A database is an organized collection of structured information, or data, typically stored electronically in a computer system. Databases are used to efficiently store, retrieve, and manage data.

## 2. Types of Databases
- **Relational Databases (RDBMS):** Store data in tables. Examples: MySQL, PostgreSQL, SQLite, Oracle.
- **NoSQL Databases:** Non-tabular, designed for scalability and flexibility. Types include document (MongoDB), key-value (Redis), column-family (Cassandra), graph (Neo4j).
- **In-memory Databases:** Data stored in RAM for fast access. Example: Redis.
- **Cloud Databases:** Managed services (AWS RDS, Google Cloud SQL).

## 3. Database Models
- **Hierarchical Model:** Tree-like structure.
- **Network Model:** Graph structure with multiple relationships.
- **Relational Model:** Tables with rows and columns.
- **Object-oriented Model:** Data as objects.

## 4. SQL Basics
SQL (Structured Query Language) is used for managing relational databases.
- `SELECT`: Retrieve data
- `INSERT`: Add data
- `UPDATE`: Modify data
- `DELETE`: Remove data
- `CREATE`: Create tables/databases
- `DROP`: Delete tables/databases

Example:
```sql
SELECT name, age FROM students WHERE age > 18;
```

## 5. Database Normalization
Normalization reduces redundancy and improves data integrity.
- **1NF:** Atomic values
- **2NF:** Remove partial dependencies
- **3NF:** Remove transitive dependencies

## 6. Transactions & ACID Properties
A transaction is a sequence of operations performed as a single logical unit.
- **Atomicity:** All or nothing
- **Consistency:** Valid state transitions
- **Isolation:** Transactions do not interfere
- **Durability:** Changes persist after commit

## 7. Indexes
Indexes speed up data retrieval. Types: primary, secondary, unique, composite.

## 8. Joins in SQL
- **INNER JOIN:** Matching rows
- **LEFT JOIN:** All rows from left, matched from right
- **RIGHT JOIN:** All rows from right, matched from left
- **FULL JOIN:** All rows from both

## 9. Backup & Recovery
- **Backup:** Copying data for protection
- **Recovery:** Restoring data after failure

## 10. Security
- Authentication & Authorization
- Encryption
- Access Control

## 11. Sample SQL Queries
```sql
-- Create table
CREATE TABLE students (
  id INT PRIMARY KEY,
  name VARCHAR(100),
  age INT
);

-- Insert data
INSERT INTO students (id, name, age) VALUES (1, 'Alice', 22);

-- Select data
SELECT * FROM students;

-- Update data
UPDATE students SET age = 23 WHERE id = 1;

-- Delete data
DELETE FROM students WHERE id = 1;
```

## 12. Further Reading
- [SQL Tutorial](https://www.w3schools.com/sql/)
- [Database Normalization](https://en.wikipedia.org/wiki/Database_normalization)
- [ACID Properties](https://en.wikipedia.org/wiki/ACID)
- [NoSQL Databases](https://www.mongodb.com/nosql-explained)

---
This guide provides a solid foundation for studying databases. Expand each section with examples and exercises for deeper learning.

## 13. Advanced SQL Concepts
- **Subqueries:** Nested queries for complex filtering.
- **Window Functions:** Aggregate data over partitions (e.g., ROW_NUMBER, RANK, SUM OVER).
- **Stored Procedures & Functions:** Encapsulate logic in the database.
- **Views:** Virtual tables for simplified queries.
- **Triggers:** Automatic actions on data changes.

## 14. Entity-Relationship (ER) Diagrams & Database Design
- **Entities:** Objects or concepts (e.g., Student, Course).
- **Relationships:** Associations between entities (e.g., Enrollment).
- **Attributes:** Properties of entities (e.g., name, age).
- **Keys:** Primary, foreign, candidate keys.
- **Design Steps:** Requirements → ER Diagram → Schema → Implementation.

## 15. Data Modeling & Schema Design
- **Normalization vs. Denormalization:** Trade-offs for performance and complexity.
- **Schema Evolution:** Handling changes over time.
- **Best Practices:** Naming conventions, documentation, constraints.

## 16. Transactions in Depth
- **Isolation Levels:** Read Uncommitted, Read Committed, Repeatable Read, Serializable.
- **Locking:** Shared, exclusive, deadlocks.
- **Concurrency Control:** Optimistic vs. pessimistic.

## 17. Indexing Strategies & Performance Tuning
- **Types of Indexes:** B-tree, hash, bitmap, full-text.
- **Query Optimization:** EXPLAIN plans, avoiding full table scans.
- **Partitioning & Sharding:** Scaling large databases.

## 18. Backup, Restore, & Disaster Recovery
- **Backup Types:** Full, incremental, differential.
- **Restore Procedures:** Point-in-time recovery, log shipping.
- **Disaster Recovery Planning:** RTO, RPO, failover strategies.

## 19. Security Best Practices
- **Roles & Permissions:** Principle of least privilege.
- **Encryption:** At rest, in transit.
- **Auditing & Monitoring:** Track access and changes.

## 20. NoSQL Deep Dive
- **Types:** Document, key-value, column-family, graph.
- **CAP Theorem:** Consistency, Availability, Partition Tolerance.
- **Use Cases:** When to choose NoSQL over RDBMS.
- **Data Modeling:** Flexible schemas, denormalization.

## 21. Real-World Case Studies
- **E-commerce Database:** Products, orders, customers, inventory.
- **Social Network:** Users, posts, comments, relationships.
- **Banking System:** Accounts, transactions, audits, security.

## 22. Practice Exercises
### SQL Challenges
1. Write a query to find the top 3 oldest students.
2. Create a table for courses and enrollments with foreign keys.
3. Write a transaction that transfers money between accounts.
4. Design an ER diagram for a library system.
5. Normalize a table with redundant data to 3NF.

### NoSQL Challenges
1. Model a blog platform in MongoDB.
2. Design a key-value store for session management.

### Security & Backup
1. Set up user roles for a database.
2. Plan a backup strategy for a critical system.

## 23. Solutions & Explanations
- Detailed solutions for each exercise (add your answers and compare).

## 24. Visual Aids
- Use online tools for ER diagrams (dbdiagram.io, Lucidchart).
- Query visualizers (SQL Fiddle, DataGrip).

## 25. Additional Resources
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [MongoDB University](https://university.mongodb.com/)
- [SQLZoo Practice](https://sqlzoo.net/)
- [Database Design Patterns](https://www.databasedesignpatterns.com/)

---
This expanded guide covers everything needed for deep and practical database study. Work through the exercises, diagrams, and case studies for mastery.