import sqlite3
import pandas as pd

# ── Connection ───────────────────────────────────────────────
conn = sqlite3.connect("day9.db")
cursor = conn.cursor()

# ── Create Tables ────────────────────────────────────────────
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        course_id INTEGER,
        score REAL,
        passed INTEGER
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_name TEXT NOT NULL,
        instructor TEXT
    )
""")

# ── Insert Data ──────────────────────────────────────────────
cursor.executemany("""
    INSERT INTO courses (course_name, instructor)
    VALUES (?, ?)
""", [
    ("ML Basics", "Dr. Smith"),
    ("Deep Learning", "Dr. Lee"),
    ("NLP", "Dr. Patel"),
])

cursor.executemany("""
    INSERT INTO students (name, course_id, score, passed)
    VALUES (?, ?, ?, ?)
""", [
    ("Alice", 1, 92.5, 1),
    ("Bob", 1, 45.0, 0),
    ("Charlie", 2, 78.3, 1),
    ("Diana", 2, 88.0, 1),
    ("Eve", 1, 55.5, 0),
    ("Frank", 2, 95.0, 1),
    ("Grace", 3, 40.0, 0),
    ("Hank", 3, 72.0, 1),
    ("Ivan", None, 80.0, 1),  # no course assigned
])

conn.commit()

# ── INNER JOIN ───────────────────────────────────────────────
print("\n--- INNER JOIN: Students with their Course ---")
df = pd.read_sql_query("""
    SELECT students.name, students.score, courses.course_name, courses.instructor
    FROM students
    INNER JOIN courses ON students.course_id = courses.id
""", conn)
print(df)

# ── LEFT JOIN ────────────────────────────────────────────────
print("\n--- LEFT JOIN: All Students (with or without course) ---")
df = pd.read_sql_query("""
    SELECT students.name, students.score, courses.course_name
    FROM students
    LEFT JOIN courses ON students.course_id = courses.id
""", conn)
print(df)

# ── Subquery in WHERE ────────────────────────────────────────
print("\n--- Subquery: Students Above Average Score ---")
df = pd.read_sql_query("""
    SELECT name, score
    FROM students
    WHERE score > (SELECT AVG(score) FROM students)
""", conn)
print(df)

# ── Subquery in SELECT ───────────────────────────────────────
print("\n--- Subquery in SELECT: Score vs Average ---")
df = pd.read_sql_query("""
    SELECT 
        name, 
        score,
        (SELECT AVG(score) FROM students) AS avg_score,
        score - (SELECT AVG(score) FROM students) AS diff_from_avg
    FROM students
""", conn)
print(df)

# ── Exercise 1: INNER JOIN - name, score, instructor ─────────
print("\n--- Exercise 1: Student Name, Score, Instructor ---")
df_ex1 = pd.read_sql_query("""
    SELECT students.name, students.score, courses.instructor
    FROM students
    INNER JOIN courses ON students.course_id = courses.id
""", conn)
print(df_ex1)

# ── Exercise 2: LEFT JOIN - students with no course ──────────
print("\n--- Exercise 2: Students with No Course ---")
df_ex2 = pd.read_sql_query("""
    SELECT students.name, students.score, courses.course_name
    FROM students
    LEFT JOIN courses ON students.course_id = courses.id
    WHERE courses.course_name IS NULL
""", conn)
print(df_ex2)

# ── Exercise 3: Subquery - scored above max failed score ─────
print("\n--- Exercise 3: Above Max Failed Score ---")
df_ex3 = pd.read_sql_query("""
    SELECT name, score
    FROM students
    WHERE score > (SELECT MAX(score) FROM students WHERE passed = 0)
""", conn)
print(df_ex3)

# ── Exercise 4: INNER JOIN + GROUP BY - avg score per instructor
print("\n--- Exercise 4: Avg Score per Instructor ---")
df_ex4 = pd.read_sql_query("""
    SELECT courses.instructor, AVG(students.score) AS avg_score
    FROM students
    INNER JOIN courses ON students.course_id = courses.id
    GROUP BY courses.instructor
""", conn)
print(df_ex4)

# ── Exercise 5: Students above their course average ──────────
print("\n--- Exercise 5: Students Above Their Course Average ---")
df_ex5 = pd.read_sql_query("""
    SELECT students.name, students.score, courses.course_name
    FROM students
    INNER JOIN courses ON students.course_id = courses.id
    WHERE students.score > (
        SELECT AVG(s2.score)
        FROM students s2
        WHERE s2.course_id = students.course_id
    )
""", conn)
print(df_ex5)

# ── Close connection ─────────────────────────────────────────
conn.close()
print("\nDone! Database connection closed.")