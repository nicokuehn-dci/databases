

# All-in-one Database Tutor
lessons = {
    "Introduction to Databases": "A database is an organized collection of structured information, typically stored electronically.",
    "Types of Databases": "Relational, NoSQL, In-memory, Cloud databases.",
    "Database Models": "Hierarchical, Network, Relational, Object-oriented.",
    "SQL Basics": "SQL is used for managing relational databases. Key commands: SELECT, INSERT, UPDATE, DELETE, CREATE, DROP.",
    "Database Normalization": "Normalization reduces redundancy and improves data integrity. 1NF, 2NF, 3NF.",
    "Transactions & ACID Properties": "Atomicity, Consistency, Isolation, Durability.",
    "Indexes": "Indexes speed up data retrieval. Types: primary, secondary, unique, composite.",
    "Joins in SQL": "INNER, LEFT, RIGHT, FULL JOINs.",
    "Backup & Recovery": "Backup: copying data. Recovery: restoring data after failure.",
    "Security": "Authentication, Authorization, Encryption, Access Control.",
    "Sample SQL Queries": "CREATE TABLE, INSERT, SELECT, UPDATE, DELETE.",
    "Advanced SQL Concepts": "Subqueries, window functions, stored procedures, views, triggers.",
    "ER Diagrams & Database Design": "Entities, relationships, attributes, keys, design steps.",
    "Data Modeling & Schema Design": "Normalization vs. denormalization, schema evolution, best practices.",
    "Transactions in Depth": "Isolation levels, locking, concurrency control.",
    "Indexing & Performance Tuning": "B-tree, hash, bitmap, full-text indexes, query optimization.",
    "Backup, Restore, & Disaster Recovery": "Full, incremental, differential backups, restore procedures, disaster recovery planning.",
    "Security Best Practices": "Roles, permissions, encryption, auditing, monitoring.",
    "NoSQL Deep Dive": "Document, key-value, column-family, graph databases, CAP theorem, use cases.",
    "Real-World Case Studies": "E-commerce, social network, banking system databases."
}
quizzes = {
    "Introduction to Databases": [
        ("What is a database?", "An organized collection of structured information or data."),
        ("Name one purpose of a database.", "Efficient data storage, retrieval, and management.")
    ],
    "SQL Basics": [
        ("Which SQL command is used to retrieve data?", "SELECT"),
        ("Write a SQL query to select all students older than 18.", "SELECT * FROM students WHERE age > 18;")
    ],
    "Database Normalization": [
        ("What is the goal of normalization?", "Reduce redundancy and improve data integrity."),
        ("Name the first three normal forms.", "1NF, 2NF, 3NF")
    ]
}
exercises = {
    "SQL Basics": [
        "Write a query to find the top 3 oldest students.",
        "Create a table for courses and enrollments with foreign keys."
    ],
    "NoSQL": [
        "Model a blog platform in MongoDB.",
        "Design a key-value store for session management."
    ],
    "Security": [
        "Set up user roles for a database.",
        "Plan a backup strategy for a critical system."
    ]
}
projects = [
    "Design and implement an e-commerce database (products, orders, customers, inventory).",
    "Create a social network schema (users, posts, comments, relationships).",
    "Build a banking system database (accounts, transactions, audits, security)."
]

def main():
    print("\n=== Database Tutor: All-in-One Study Guide ===\n")
    for topic, content in lessons.items():
        print(f"\n--- {topic} ---\n{content}")

    print("\n=== Practice Exercises ===")
    for topic, exs in exercises.items():
        print(f"\n{topic} Exercises:")
        for ex in exs:
            print(f"- {ex}")

    print("\n=== Mini-Projects ===")
    for proj in projects:
        print(f"- {proj}")

    print("\n=== Quizzes (Sample Questions) ===")
    for topic, questions in quizzes.items():
        print(f"\n{topic} Quizzes:")
        for q, a in questions:
            print(f"Q: {q}")
            print(f"Sample answer: {a}\n")

    print("\n=== Additional Resources ===")
    print("- SQL Tutorial: https://www.w3schools.com/sql/")
    print("- Database Normalization: https://en.wikipedia.org/wiki/Database_normalization")
    print("- ACID Properties: https://en.wikipedia.org/wiki/ACID")
    print("- NoSQL Databases: https://www.mongodb.com/nosql-explained")
    print("- PostgreSQL Documentation: https://www.postgresql.org/docs/")
    print("- MongoDB University: https://university.mongodb.com/")
    print("- SQLZoo Practice: https://sqlzoo.net/")
    print("- Database Design Patterns: https://www.databasedesignpatterns.com/")

    print("\n=== End of Guide ===")

if __name__ == "__main__":
    main()
