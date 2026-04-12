import numpy as np

# =========================
# CHALLENGE 1 — DataSet Class
# =========================
# normalize() = min-max scaling → same as sklearn's MinMaxScaler
# formula: (x - min) / (max - min) → scales everything to 0-1

class DataSet:
    def __init__(self, data):
        self.data = data

    def mean(self):
        return sum(self.data) / len(self.data)

    def variance(self):
        m = self.mean()
        return sum((x - m)**2 for x in self.data) / len(self.data)

    def std(self):
        return self.variance() ** 0.5

    def normalize(self):
        min_val = min(self.data)
        max_val = max(self.data)
        return [(x - min_val) / (max_val - min_val) for x in self.data]

    def summary(self):
        print("Mean:", self.mean())
        print("Variance:", self.variance())
        print("Std Dev:", self.std())
        print("Normalized:", self.normalize())

ds = DataSet([10, 20, 30, 40, 50])
print("Challenge 1:")
ds.summary()
print()

# =========================
# CHALLENGE 2 — Matrix Multiply from Scratch
# =========================
# Rule: (m×n) @ (n×p) = (m×p)
# For each output cell [i][j]:
# sum of row i from A × column j from B

def matrix_multiply(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    cols_B = len(B[0])

    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):   # ✅ correct loop
                result[i][j] += A[i][k] * B[k][j]

    return result