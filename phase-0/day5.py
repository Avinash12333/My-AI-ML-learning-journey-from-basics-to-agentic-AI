import numpy as np
import matplotlib.pyplot as plt

# =========================
# Exercise 1 — Normal Distribution
# =========================
data = np.random.normal(0, 1, 1000)

print("Exercise 1:")
print("Mean:", np.mean(data))
print("Std:", np.std(data))

plt.hist(data, bins=30)
plt.title("Normal Distribution (mean=0, std=1)")
plt.show()


# =========================
# Exercise 2 — Manual Stats
# =========================
arr = np.array([2, 4, 4, 4, 5, 5, 7, 9])

# Manual mean
mean = sum(arr) / len(arr)

# Manual variance
variance = sum((x - mean)**2 for x in arr) / len(arr)

# Manual std
std = np.sqrt(variance)

print("\nExercise 2:")
print("Manual Mean:", mean)
print("Manual Std:", std)

print("NumPy Mean:", np.mean(arr))
print("NumPy Std:", np.std(arr))


# =========================
# Exercise 3 — Correlation
# =========================
x = np.random.normal(0, 1, 1000)
noise = np.random.normal(0, 1, 1000)
y = 2*x + noise

corr = np.corrcoef(x, y)[0, 1]

print("\nExercise 3:")
print("Correlation:", corr)

plt.scatter(x, y)
plt.title("x vs y (correlated)")
plt.show()


# =========================
# Exercise 4 — Changing Std
# =========================
x_vals = np.linspace(-5, 5, 100)

y1 = (1/(0.5*np.sqrt(2*np.pi))) * np.exp(-(x_vals**2)/(2*0.5**2))
y2 = (1/(1*np.sqrt(2*np.pi))) * np.exp(-(x_vals**2)/(2*1**2))
y3 = (1/(2*np.sqrt(2*np.pi))) * np.exp(-(x_vals**2)/(2*2**2))

plt.plot(x_vals, y1, label="std=0.5")
plt.plot(x_vals, y2, label="std=1.0")
plt.plot(x_vals, y3, label="std=2.0")

plt.legend()
plt.title("Effect of Standard Deviation")
plt.show()


# =========================
# Exercise 5 — Central Limit Theorem
# =========================
means = []

for _ in range(1000):
    rolls = np.random.randint(1, 7, 30)  # 30 dice
    means.append(np.mean(rolls))

plt.hist(means, bins=30)
plt.title("Central Limit Theorem (Dice Averages)")
plt.show()