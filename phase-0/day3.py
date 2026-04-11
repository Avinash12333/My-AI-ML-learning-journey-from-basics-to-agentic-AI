import numpy as np

# =========================
# Exercise 1 — Dot Product
# =========================
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Manual
manual_dot = sum(x * y for x, y in zip(a, b))

# NumPy
numpy_dot = np.dot(a, b)

print("Exercise 1:")
print("Manual Dot:", manual_dot)
print("NumPy Dot:", numpy_dot)
print()


# =========================
# Exercise 2 — Matrix Multiplication
# =========================
A = np.array([[1, 2, 3],
              [4, 5, 6]])   # (2,3)

B = np.array([[7, 8],
              [9, 10],
              [11, 12]])    # (3,2)

result = A @ B

print("Exercise 2:")
print("Result:\n", result)
print("Shape:", result.shape)  # Expected (2,2)
print()


# =========================
# Exercise 3 — Transpose
# =========================
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

print("Exercise 3:")
print("Original:\n", A)
print("Transpose:\n", A.T)
print()


# =========================
# Exercise 4 — Fix Shape Error
# =========================
A = np.array([[1, 2, 3],
              [4, 5, 6]])   # (2,3)

B = np.array([[7, 8, 9],
              [10, 11, 12]])  # (2,3) ❌ wrong

# Fix: transpose B → (3,2)
B_fixed = B.T

result = A @ B_fixed

print("Exercise 4:")
print("Fixed Result:\n", result)
print()


# =========================
# Exercise 5 — Cosine Similarity
# =========================
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

dot = np.dot(a, b)
mag_a = np.linalg.norm(a)
mag_b = np.linalg.norm(b)

cos_sim = dot / (mag_a * mag_b)

print("Exercise 5:")
print("Cosine Similarity:", cos_sim)  # ~0.9746