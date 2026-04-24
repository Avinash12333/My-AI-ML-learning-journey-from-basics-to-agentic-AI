import pandas as pd
import numpy as np

# ── Create Dataset ───────────────────────────────────────────
data = {
    "name":     ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Bob", None],
    "age":      [25, 30, None, 28, 22, 35, 29, 30, 27],
    "score":    [92.5, 45.0, 78.3, 88.0, 55.5, 95.0, 40.0, 45.0, 80.0],
    "course":   ["ML", "DL", "NLP", "ML", "DL", "NLP", "ML", "DL", "NLP"],
    "passed":   [1, 0, 1, 1, 0, 1, 0, 0, 1],
    "grade":    ["A", "F", "B", "A", "D", "A", "F", "F", "B"],
}

df = pd.DataFrame(data)
print("\n--- Original DataFrame ---")
print(df)

# ── Explore Data ─────────────────────────────────────────────
print("\n--- Shape ---")
print(df.shape)

print("\n--- Data Types ---")
print(df.dtypes)

print("\n--- Info ---")
print(df.info())

print("\n--- Describe ---")
print(df.describe())

print("\n--- Null Counts ---")
print(df.isnull().sum())

# ── Clean Data ───────────────────────────────────────────────
df = df.drop_duplicates()
print("\n--- After Dropping Duplicates ---")
print(df.shape)

df["age"] = df["age"].fillna(df["age"].median())
df["name"] = df["name"].fillna("Unknown")

print("\n--- After Filling Nulls ---")
print(df.isnull().sum())

# ── Transform Data ───────────────────────────────────────────
df = df.rename(columns={"score": "final_score"})

df["score_category"] = df["final_score"].apply(
    lambda x: "High" if x >= 80 else ("Medium" if x >= 60 else "Low")
)

df["result"] = df["passed"].map({1: "Pass", 0: "Fail"})

print("\n--- After Transformations ---")
print(df)

# ── Merge DataFrames ─────────────────────────────────────────
instructors = pd.DataFrame({
    "course":     ["ML", "DL", "NLP"],
    "instructor": ["Dr. Smith", "Dr. Lee", "Dr. Patel"],
})

df_merged = pd.merge(df, instructors, on="course", how="left")
print("\n--- Merged DataFrame ---")
print(df_merged)

# ── Group & Aggregate ────────────────────────────────────────
df_grouped = df.groupby("course").agg(
    num_students=("name", "count"),
    avg_score=("final_score", "mean"),
    pass_count=("passed", "sum")
).reset_index()

print("\n--- Grouped by Course ---")
print(df_grouped)

# ── Exercise 1: Students who scored > 70 and passed ──────────
print("\n--- Exercise 1: Score > 70 and Passed ---")
df_ex1 = df[(df["final_score"] > 70) & (df["passed"] == 1)]
print(df_ex1)

# ── Exercise 2: Add bonus_score column ───────────────────────
print("\n--- Exercise 2: Bonus Score ---")
df["bonus_score"] = df.apply(
    lambda row: row["final_score"] + 5 if row["passed"] == 1 else row["final_score"],
    axis=1
)
print(df[["name", "final_score", "passed", "bonus_score"]])

# ── Exercise 3: Group by grade ───────────────────────────────
print("\n--- Exercise 3: Group by Grade ---")
df_ex3 = df.groupby("grade").agg(
    count=("name", "count"),
    avg_score=("final_score", "mean")
).reset_index()
print(df_ex3)

# ── Exercise 4: NLP students with instructor ─────────────────
print("\n--- Exercise 4: NLP Students with Instructor ---")
df_ex4 = pd.merge(df, instructors, on="course", how="left")
df_ex4 = df_ex4[df_ex4["course"] == "NLP"][["name", "final_score", "course", "instructor"]]
print(df_ex4)

# ── Exercise 5: Course with highest avg score (passed only) ──
print("\n--- Exercise 5: Best Course (Passed Students Only) ---")
df_passed = df[df["passed"] == 1]
df_ex5 = df_passed.groupby("course")["final_score"].mean()
best_course = df_ex5.idxmax()
print(f"Course with highest avg score among passed students: {best_course}")
print(df_ex5.sort_values(ascending=False))