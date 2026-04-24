import sqlite3
import pandas as pd

# ── Connection ──────────────────────────────────────────────
conn = sqlite3.connect("ml_study.db")
cursor = conn.cursor()

# ── Create Table ─────────────────────────────────────────────
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        score REAL,
        course TEXT,
        passed INTEGER
    )
""")

# ── Insert Data ──────────────────────────────────────────────
students_data = [
    ("Alice", 92.5, "ML Basics", 1),
    ("Bob", 45.0, "ML Basics", 0),
    ("Charlie", 78.3, "Deep Learning", 1),
    ("Diana", 88.0, "Deep Learning", 1),
    ("Eve", 55.5, "ML Basics", 0),
    ("Frank", 95.0, "Deep Learning", 1),
    ("Grace", 40.0, "NLP", 0),
    ("Hank", 72.0, "NLP", 1),
]

cursor.executemany("""
    INSERT INTO students (name, score, course, passed)
    VALUES (?, ?, ?, ?)
""", students_data)

conn.commit()

# ── Basic Queries ────────────────────────────────────────────
print("\n--- All Students ---")
df = pd.read_sql_query("SELECT * FROM students", conn)
print(df)

print("\n--- Passed Students ---")
df_passed = pd.read_sql_query("SELECT * FROM students WHERE passed = 1", conn)
print(df_passed)

print("\n--- Sorted by Score (DESC) ---")
df_sorted = pd.read_sql_query("SELECT * FROM students ORDER BY score DESC", conn)
print(df_sorted)

print("\n--- Top 3 Students ---")
df_top3 = pd.read_sql_query("SELECT * FROM students ORDER BY score DESC LIMIT 3", conn)
print(df_top3)

# ── Aggregates ───────────────────────────────────────────────
print("\n--- Aggregate Stats ---")
df_agg = pd.read_sql_query("""
    SELECT 
        COUNT(*) as total_students,
        AVG(score) as avg_score,
        MAX(score) as top_score,
        MIN(score) as lowest_score
    FROM students
""", conn)
print(df_agg)

print("\n--- Stats by Course ---")
df_by_course = pd.read_sql_query("""
    SELECT 
        course,
        COUNT(*) as num_students,
        AVG(score) as avg_score,
        SUM(passed) as num_passed
    FROM students
    GROUP BY course
""", conn)
print(df_by_course)

print("\n--- Courses with Avg Score > 70 (HAVING) ---")
df_having = pd.read_sql_query("""
    SELECT course, AVG(score) as avg_score
    FROM students
    GROUP BY course
    HAVING AVG(score) > 70
""", conn)
print(df_having)

# ── Exercise 1: NLP students sorted by score DESC ────────────
print("\n--- Exercise 1: NLP Students ---")
df_ex1 = pd.read_sql_query("""
    SELECT * FROM students
    WHERE course = 'NLP'
    ORDER BY score DESC
""", conn)
print(df_ex1)

# ── Exercise 2: Total failed students ────────────────────────
print("\n--- Exercise 2: Failed Students ---")
df_ex2 = pd.read_sql_query("""
    SELECT COUNT(*) AS failed_students
    FROM students
    WHERE passed = 0
""", conn)
print(df_ex2)

# ── Exercise 3: Highest score per course ─────────────────────
print("\n--- Exercise 3: Highest Score per Course ---")
df_ex3 = pd.read_sql_query("""
    SELECT course, MAX(score) AS highest_score
    FROM students
    GROUP BY course
""", conn)
print(df_ex3)

# ── Exercise 4: Students scoring between 70 and 90 ───────────
print("\n--- Exercise 4: Scores Between 70 and 90 ---")
df_ex4 = pd.read_sql_query("""
    SELECT name, score
    FROM students
    WHERE score BETWEEN 70 AND 90
""", conn)
print(df_ex4)

# ── Exercise 5: Add 5 students + pass rate ───────────────────
cursor.executemany("""
    INSERT INTO students (name, course, score, passed)
    VALUES (?, ?, ?, ?)
""", [
    ("Alex", "NLP", 85, 1),
    ("Sam", "ML Basics", 60, 0),
    ("John", "Deep Learning", 92, 1),
    ("Emma", "NLP", 74, 1),
    ("Lily", "ML Basics", 68, 0),
])
conn.commit()

print("\n--- Exercise 5: Overall Pass Rate ---")
df_ex5 = pd.read_sql_query("""
    SELECT (SUM(passed) * 100.0) / COUNT(*) AS pass_rate_percentage
    FROM students
""", conn)
print(df_ex5)

# ── Close connection ─────────────────────────────────────────
conn.close()
print("\nDone! Database connection closed.")