import pandas as pd
import numpy as np

# ── Raw Dataset ──────────────────────────────────────────────
data = {
    "name":     ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Hank", None],
    "age":      [25, 30, None, 28, 22, 35, 29, None, 27],
    "score":    [92.5, 45.0, 78.3, 88.0, 55.5, 95.0, 40.0, 72.0, 80.0],
    "course":   ["ML", "DL", "NLP", "ML", "DL", "NLP", "ML", "DL", "NLP"],
    "passed":   [1, 0, 1, 1, 0, 1, 0, 1, 1],
    "city":     ["NYC", "LA", "NYC", "Chicago", "LA", "NYC", "Chicago", "LA", None],
}

print("--- Raw Data ---")
print(pd.DataFrame(data))

# ── Pipeline Functions ───────────────────────────────────────
def load_data(data):
    """Load raw data into a DataFrame"""
    return pd.DataFrame(data)

def clean_data(df):
    """Handle nulls and duplicates"""
    df = df.drop_duplicates()
    df["age"] = df["age"].fillna(df["age"].median())
    df["name"] = df["name"].fillna("Unknown")
    df["city"] = df["city"].fillna("Unknown")
    return df

def engineer_features(df):
    """Create new features from existing ones"""
    df["age_group"] = pd.cut(
        df["age"],
        bins=[0, 25, 30, 100],
        labels=["Young", "Mid", "Senior"]
    )
    df["score_category"] = df["score"].apply(
        lambda x: "High" if x >= 80 else ("Medium" if x >= 60 else "Low")
    )
    df["result"] = df["passed"].map({1: "Pass", 0: "Fail"})
    return df

def scale_features(df):
    """Min-max normalize score and age"""
    min_score = df["score"].min()
    max_score = df["score"].max()
    df["score_normalized"] = (df["score"] - min_score) / (max_score - min_score)

    # Exercise 3: normalize age as well
    min_age = df["age"].min()
    max_age = df["age"].max()
    df["age_normalized"] = (df["age"] - min_age) / (max_age - min_age)
    return df

def encode_features(df):
    """One-hot encode the course column"""
    df = pd.get_dummies(df, columns=["course"], prefix="course")
    return df

# ── Exercise 1: High Achiever Flag ───────────────────────────
def add_score_flag(df):
    """Add high_achiever column"""
    df["high_achiever"] = (df["score"] >= 85) & (df["passed"] == 1)
    return df

# ── Exercise 2: Filter DL course ─────────────────────────────
def filter_data(df):
    """Remove DL course students"""
    df = df[df["course"] != "DL"]
    return df

# ── Full Pipeline ────────────────────────────────────────────
def run_pipeline(data):
    """Run all steps in order"""
    df = load_data(data)
    df = clean_data(df)
    df = filter_data(df)       # Exercise 2
    df = engineer_features(df)
    df = scale_features(df)    # Exercise 3 included
    df = add_score_flag(df)    # Exercise 1
    df = encode_features(df)
    return df

# ── Run Pipeline ─────────────────────────────────────────────
df_final = run_pipeline(data)

print("\n--- Final Processed Data ---")
print(df_final)

print("\n--- Columns ---")
print(df_final.columns.tolist())

# ── Save & Load ──────────────────────────────────────────────
df_final.to_csv("processed_data.csv", index=False)
print("\n--- Saved to processed_data.csv ---")

df_loaded = pd.read_csv("processed_data.csv")
print("\n--- Loaded from CSV ---")
print(df_loaded.head())

# ── Exercise 4: Avg normalized score per city ────────────────
print("\n--- Exercise 4: Avg Score Normalized per City ---")
df_ex4 = df_final.groupby("city")["score_normalized"].mean().reset_index()
df_ex4.columns = ["city", "avg_score_normalized"]
print(df_ex4)

# ── Exercise 5: Save high achievers to CSV ───────────────────
print("\n--- Exercise 5: Top Students ---")
df_top = df_final[df_final["high_achiever"] == True]
df_top.to_csv("top_students.csv", index=False)
print(f"Saved {len(df_top)} top students to top_students.csv")
print(df_top[["name", "score", "passed", "high_achiever"]])