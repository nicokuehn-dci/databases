# Mini Program: Connect to SQLite and run a query
import sqlite3

# Connect to database (creates file if it doesn't exist)
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# Create table
cursor.execute('CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)')

# Insert sample data
cursor.execute('INSERT INTO students (name, age) VALUES (?, ?)', ('Bob', 21))
conn.commit()

# Query data
for row in cursor.execute('SELECT * FROM students'):
    print(row)

# Challenge: Add another student and print all students
# cursor.execute('INSERT INTO students (name, age) VALUES (?, ?)', ('Eve', 23))
# conn.commit()
# for row in cursor.execute('SELECT * FROM students'):
#     print(row)

conn.close()
