import sqlite3
import pandas as pd

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

# --- Setup ---
cursor.executescript("""
CREATE TABLE departments (
    id INTEGER PRIMARY KEY,
    name TEXT,
    budget INTEGER
);

CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    score REAL,
    dept_id INTEGER
);

INSERT INTO departments VALUES (1, 'Engineering', 90000);
INSERT INTO departments VALUES (2, 'Science', 75000);
INSERT INTO departments VALUES (3, 'Arts', 50000);

INSERT INTO students VALUES (1, 'Alice',  88.5, 1);
INSERT INTO students VALUES (2, 'Bob',    62.0, 2);
INSERT INTO students VALUES (3, 'Sara',   91.0, 1);
INSERT INTO students VALUES (4, 'James',  55.5, 3);
INSERT INTO students VALUES (5, 'Priya',  78.0, 2);
INSERT INTO students VALUES (6, 'Emma',   95.0, 1);
INSERT INTO students VALUES (7, 'Carlos', 69.5, 3);
""")
conn.commit()
print("✅ Database ready!")

# --- Exercise 1: SELECT + WHERE ---
# Get all students with score above 70
df = pd.read_sql_query("SELECT * FROM students WHERE score > 70", conn)
print("Exercise 1 — Students with score > 70:")
print(df)
print()

# --- Exercise 2: ORDER BY + LIMIT ---
# Get top 3 students by score
df = pd.read_sql_query("SELECT * FROM students ORDER BY score DESC LIMIT 3", conn)
print("Exercise 2 — Top 3 students:")
print(df)
print()

# --- Exercise 3: GROUP BY + Aggregation ---
# Get average score per department
df = pd.read_sql_query(
    "SELECT dept_id, AVG(score) as avg_score FROM students GROUP BY dept_id", conn
)
print("Exercise 3 — Avg score per department:")
print(df)
print()

# --- Exercise 4: INNER JOIN ---
# Get student name, score, and department name
df = pd.read_sql_query("""
    SELECT s.name, s.score, d.name as department
    FROM students s
    INNER JOIN departments d ON s.dept_id = d.id
""", conn)
print("Exercise 4 — Students with department names:")
print(df)
print()

# --- Exercise 5: Window Function ---
# Rank students by score within each department
df = pd.read_sql_query("""
    SELECT s.name, d.name as department, s.score,
           RANK() OVER (PARTITION BY d.name ORDER BY s.score DESC) as rank
    FROM students s
    INNER JOIN departments d ON s.dept_id = d.id
""", conn)
print("Exercise 5 — Ranked students per department:")
print(df)
print()

conn.close()
