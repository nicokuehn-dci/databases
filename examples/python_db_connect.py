# Example: Python program to connect to a SQLite database
import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)')
cursor.execute('INSERT INTO students (name, age) VALUES (?, ?)', ('Alice', 22))
conn.commit()
for row in cursor.execute('SELECT * FROM students'):
    print(row)
conn.close()
