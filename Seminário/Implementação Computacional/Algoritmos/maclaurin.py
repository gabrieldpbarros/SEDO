import numpy as np
import matplotlib.pyplot as plt
import time
from scipy.special import factorial

# Define the functions
def exp_func(x):
    return np.exp(x)

def ln_func(x):
    return np.log(1 + x)

def sin_func(x):
    return np.sin(x)

# Maclaurin series for e^x
def maclaurin_exp(x, terms):
    """Maclaurin series for e^x using numpy."""
    n = np.arange(terms)
    return np.sum((x[:, np.newaxis]**n) / factorial(n), axis=1)

# Maclaurin series for ln(1+x)
def maclaurin_ln(x, terms):
    """Maclaurin series for ln(1+x) using numpy."""
    n = np.arange(1, terms + 1)
    return np.sum(((-1)**(n + 1)) * (x[:, np.newaxis]**n) / n, axis=1)

def maclaurin_sin(x, terms):
    """MacLaurin series for sin(x) using numpy."""
    n = np.arange(terms)
    return np.sum(((-1)**n) * (x[:, np.newaxis]**(2 * n + 1)) / factorial(2 * n + 1), axis=1)

# Parameters
x_values_exp = np.linspace(-6, 6, 1000)  # Interval for approximation
x_values_ln = np.linspace(-1, 1, 1000)
x_values_sin = np.linspace(-6, 6, 1000)

# Initialize lists to store results
y_exp = []
y_ln = []
y_sin = []

# Approximate e^x using Maclaurin series
start_exp = time.time()
for i in range(1, 11, 2):
    y_exp.append(maclaurin_exp(x_values_exp, terms=i + 1))
end_exp = time.time()
print(f"e^x execution time: {end_exp - start_exp:.6f} seconds")

# Approximate ln(1+x) using Maclaurin series
start_ln = time.time()
for i in range(5):
    y_ln.append(maclaurin_ln(x_values_ln, terms=5 * (i + 1)))
end_ln = time.time()
print(f"ln(1+x) execution time: {end_ln - start_ln:.6f} seconds")

# Approximate sin(x) using Maclaurin series
start_sin = time.time()
for i in range(0, 10, 2):
    y_sin.append(maclaurin_sin(x_values_sin, terms=i + 1))
end_sin = time.time()
print(f"sin(x) execution time: {end_sin - start_sin:.6f} seconds")

# Plot the results
plt.figure(figsize=(18, 6))

# Plot e^x approximation
plt.subplot(1, 3, 1)
plt.plot(x_values_exp, exp_func(x_values_exp), label="e^x")
for i in range(1, 11, 2):
    plt.plot(x_values_exp, y_exp[(i-1)//2], label=f"Série de Maclaurin (n = {i + 1})")
plt.title("Aproximação de e^x pela Série de Maclaurin")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid()

# Plot ln(1+x) approximation
plt.subplot(1, 3, 2)
plt.plot(x_values_ln, ln_func(x_values_ln), label="ln(1+x)")
for i in range(5):
    plt.plot(x_values_ln, y_ln[i], label=f"Série de Maclaurin (n = {5 * (i + 1)})")
plt.title("Aproximação de ln(1+x) pela Série de Maclaurin")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid()

# Plot sin(x) approximation
plt.subplot(1, 3, 3)
plt.plot(x_values_ln, sin_func(x_values_ln), label="sen(x)")
for i in range(0, 10, 2):
    plt.plot(x_values_sin, y_sin[i//2], label=f"Série de Maclaurin (n = {i + 1})")
plt.title("Aproximação de sen(x) pela Série de Maclaurin")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.ylim(-2, 2)
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()