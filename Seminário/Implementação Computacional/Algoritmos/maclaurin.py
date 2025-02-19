import numpy as np
import matplotlib.pyplot as plt
import time
from scipy.special import factorial

# Define the functions
def exp_func(x):
    return np.exp(x)

def ln_func(x):
    return np.log(1 + x)

# Optimized Maclaurin series for e^x
def maclaurin_exp_optimized(x, terms):
    """Optimized Maclaurin series for e^x using numpy."""
    n = np.arange(terms)
    return np.sum((x[:, np.newaxis]**n) / factorial(n), axis=1)

# Optimized Maclaurin series for ln(1+x)
def maclaurin_ln_optimized(x, terms):
    """Optimized Maclaurin series for ln(1+x) using numpy."""
    n = np.arange(1, terms + 1)
    return np.sum(((-1)**(n + 1)) * (x[:, np.newaxis]**n) / n, axis=1)

# Parameters
x_values = np.linspace(-1, 1, 1000)  # Interval for approximation

# Initialize lists to store results
y_exp = []
y_ln = []

# Approximate e^x using optimized Maclaurin series
start_exp = time.time()
for i in range(4):
    y_exp.append(maclaurin_exp_optimized(x_values, terms=i + 1))
end_exp = time.time()
print(f"e^x execution time: {end_exp - start_exp:.6f} seconds")

# Approximate ln(1+x) using optimized Maclaurin series
start_ln = time.time()
for i in range(3):
    y_ln.append(maclaurin_ln_optimized(x_values, terms=5 * (i + 1)))
end_ln = time.time()
print(f"ln(1+x) execution time: {end_ln - start_ln:.6f} seconds")

# Plot the results
plt.figure(figsize=(18, 6))

# Plot e^x approximation
plt.subplot(1, 2, 1)
plt.plot(x_values, exp_func(x_values), label="e^x")
for i in range(4):
    plt.plot(x_values, y_exp[i], label=f"Série de Maclaurin para qt.termos = {i + 1}")
plt.title("Aproximação de e^x pela Série de Maclaurin")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid()

# Plot ln(1+x) approximation
plt.subplot(1, 2, 2)
plt.plot(x_values, ln_func(x_values), label="ln(1+x)")
for i in range(3):
    plt.plot(x_values, y_ln[i], label=f"Série de Maclaurin para qt.termos = {5 * (i + 1)}")
plt.title("Aproximação de ln(1+x) pela Série de Maclaurin")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()