-- Mini Program: SQL JOIN Example
CREATE TABLE IF NOT EXISTS students (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);
CREATE TABLE IF NOT EXISTS courses (
    id INT PRIMARY KEY,
    title VARCHAR(100)
);
CREATE TABLE IF NOT EXISTS enrollments (
    student_id INT,
    course_id INT
);

-- Insert sample data
INSERT INTO students (id, name) VALUES (1, 'Alice'), (2, 'Bob');
INSERT INTO courses (id, title) VALUES (1, 'Math'), (2, 'History');
INSERT INTO enrollments (student_id, course_id) VALUES (1, 1), (2, 2);

-- Query: List students and their courses
SELECT students.name, courses.title
FROM enrollments
JOIN students ON enrollments.student_id = students.id
JOIN courses ON enrollments.course_id = courses.id;

-- Challenge: Add a new enrollment and list all enrollments
