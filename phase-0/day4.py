import numpy as np
import matplotlib.pyplot as plt

# =========================
# Exercise 1 — Derivative
# =========================
# f(x) = 3x² + 2x + 1
# f'(x) = 6x + 2  (power rule: bring down power, reduce by 1)

def f1(x):
    return 3*x**2 + 2*x + 1

def numerical_derivative(f, x, h=0.0001):
    return (f(x + h) - f(x)) / h

x = 2
print("Exercise 1:")
print("Manual derivative:", 6*x + 2)          # 14
print("Numerical derivative:", numerical_derivative(f1, x))  # ~14
print()

# =========================
# Exercise 2 — Partial Derivatives
# =========================
# f(x,y) = x²y + 3xy²
# ∂f/∂x = 2xy + 3y²  (treat y as constant)
# ∂f/∂y = x² + 6xy   (treat x as constant)

def f2(x, y):
    return x**2 * y + 3*x*y**2

def partial_x(f, x, y, h=0.0001):
    return (f(x + h, y) - f(x, y)) / h

def partial_y(f, x, y, h=0.0001):
    return (f(x, y + h) - f(x, y)) / h

x, y = 2, 3
print("Exercise 2:")
print("Manual ∂f/∂x:", 2*x*y + 3*y**2)    # 39
print("Numerical ∂f/∂x:", partial_x(f2, x, y))
print("Manual ∂f/∂y:", x**2 + 6*x*y)      # 40
print("Numerical ∂f/∂y:", partial_y(f2, x, y))
print()

# =========================
# Exercise 3 — Chain Rule
# =========================
# f(x) = (3x + 1)⁴
# f'(x) = 4(3x+1)³ × 3 = 12(3x+1)³
# Chain rule: derivative of outer × derivative of inner

def f3(x):
    return (3*x + 1)**4

x = 1
print("Exercise 3:")
print("Manual derivative:", 12*(3*x + 1)**3)       # 384
print("Numerical derivative:", numerical_derivative(f3, x))  # ~384
print()

# =========================
# Exercise 4 — Gradient Descent
# =========================
# f(x) = x² - 4x + 4
# f'(x) = 2x - 4
# Minimum is at x=2 (where f'(x) = 0)
# Gradient descent: x = x - learning_rate × gradient
# We SUBTRACT because gradient points uphill, we want downhill

def f4(x):
    return x**2 - 4*x + 4

def grad_f4(x):
    return 2*x - 4

x = 10        # start far from minimum
lr = 0.1      # learning rate
steps = 20

history = []
print("Exercise 4 — Gradient Descent:")
for i in range(steps):
    x = x - lr * grad_f4(x)
    history.append(x)
    print(f"Step {i+1}: x = {x:.4f}")

# Plot the convergence
xs = np.linspace(-1, 10, 100)
ys = f4(xs)
plt.plot(xs, ys, label="f(x) = x² - 4x + 4")
plt.scatter(history, [f4(x) for x in history], color='red', label="GD steps")
plt.title("Gradient Descent converging to minimum")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()
print()

# =========================
# Exercise 5 — Loss Gradient
# =========================
# L = (y_pred - y_true)²
# dL/dy_pred = 2(y_pred - y_true)
# This is the gradient of MSE loss used in every neural network

def loss(y_pred, y_true):
    return (y_pred - y_true)**2

def numerical_grad(y_pred, y_true, h=0.0001):
    return (loss(y_pred + h, y_true) - loss(y_pred, y_true)) / h

y_pred, y_true = 5, 3
print("Exercise 5:")
print("Manual gradient:", 2*(y_pred - y_true))     # 4
print("Numerical gradient:", numerical_grad(y_pred, y_true))  # ~4