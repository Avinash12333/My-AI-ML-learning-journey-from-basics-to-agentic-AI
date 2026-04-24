import numpy as np
import pandas as pd

# ── Part 1: NumPy Basics ─────────────────────────────────────
print("--- 1D Array ---")
arr = np.array([92.5, 45.0, 78.3, 88.0, 55.5, 95.0, 40.0, 72.0, 80.0])
print(arr)
print("Shape:", arr.shape)
print("Dtype:", arr.dtype)

print("\n--- Array Operations ---")
print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Std:", np.std(arr))
print("Min:", np.min(arr))
print("Max:", np.max(arr))
print("Sum:", np.sum(arr))

# ── Part 2: Vectorized Operations ────────────────────────────
print("\n--- Vectorized Operations ---")
print("Add 5 to all:", arr + 5)
print("Multiply by 2:", arr * 2)
print("Scores above 70:", arr[arr > 70])
print("Normalized:", (arr - arr.min()) / (arr.max() - arr.min()))

# ── Part 3: 2D Arrays (Matrices) ─────────────────────────────
print("\n--- 2D Array ---")
matrix = np.array([
    [92.5, 1, 25],
    [45.0, 0, 30],
    [78.3, 1, 28],
    [88.0, 1, 28],
    [55.5, 0, 22],
    [95.0, 1, 35],
    [40.0, 0, 29],
    [72.0, 1, 27],
    [80.0, 1, 27],
])
print(matrix)
print("Shape:", matrix.shape)
print("Scores column:", matrix[:, 0])
print("Passed column:", matrix[:, 1])
print("Ages column:", matrix[:, 2])

# ── Part 4: NumPy with Pandas ─────────────────────────────────
print("\n--- NumPy + Pandas ---")
data = {
    "name":   ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Hank", "Ivan"],
    "score":  [92.5, 45.0, 78.3, 88.0, 55.5, 95.0, 40.0, 72.0, 80.0],
    "age":    [25, 30, 28, 28, 22, 35, 29, 27, 27],
    "passed": [1, 0, 1, 1, 0, 1, 0, 1, 1],
}
df = pd.DataFrame(data)

# Use numpy operations on DataFrame columns
df["score_zscore"] = (df["score"] - np.mean(df["score"])) / np.std(df["score"])
df["score_normalized"] = (df["score"] - np.min(df["score"])) / (np.max(df["score"]) - np.min(df["score"]))
df["age_normalized"] = (df["age"] - np.min(df["age"])) / (np.max(df["age"]) - np.min(df["age"]))

print(df)

# ── Part 5: Statistical Analysis ─────────────────────────────
print("\n--- Statistical Analysis ---")
scores = df["score"].to_numpy()
print("Variance:", np.var(scores))
print("25th percentile:", np.percentile(scores, 25))
print("75th percentile:", np.percentile(scores, 75))
print("IQR:", np.percentile(scores, 75) - np.percentile(scores, 25))

# ── Exercise 1: Vectorized score bonus ───────────────────────
print("\n--- Exercise 1: Score Bonus ---")
passed = df["passed"].to_numpy()
scores = df["score"].to_numpy()
bonus_scores = np.where(passed == 1, scores + 5, scores)
df["bonus_score"] = bonus_scores
print(df[["name", "score", "passed", "bonus_score"]])

# ── Exercise 2: Classify scores using np.where ───────────────
print("\n--- Exercise 2: Score Classification ---")
df["category"] = np.where(
    df["score"] >= 80, "High",
    np.where(df["score"] >= 60, "Medium", "Low")
)
print(df[["name", "score", "category"]])

# ── Exercise 3: Matrix column stats ──────────────────────────
print("\n--- Exercise 3: Matrix Column Stats ---")
print("Avg score:", np.mean(matrix[:, 0]))
print("Pass rate:", np.mean(matrix[:, 1]) * 100, "%")
print("Avg age:", np.mean(matrix[:, 2]))
print("Highest score:", np.max(matrix[:, 0]))
print("Lowest score:", np.min(matrix[:, 0]))

# ── Exercise 4: Z-score outlier detection ────────────────────
print("\n--- Exercise 4: Outlier Detection (Z-score) ---")
zscores = df["score_zscore"].to_numpy()
outliers = df[np.abs(zscores) > 1.5]
print("Outliers (|zscore| > 1.5):")
print(outliers[["name", "score", "score_zscore"]])

# ── Exercise 5: Correlation between age and score ────────────
print("\n--- Exercise 5: Correlation ---")
ages = df["age"].to_numpy()
scores = df["score"].to_numpy()
correlation = np.corrcoef(ages, scores)
print("Correlation matrix (age vs score):")
print(correlation)
print(f"Correlation coefficient: {correlation[0, 1]:.4f}")

# ── Save final DataFrame ──────────────────────────────────────
df.to_csv("day12_processed.csv", index=False)
print("\n--- Saved to day12_processed.csv ---")
print("Done!")