import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import time

def exp_func(x):
    return np.exp(x)

def ln_func(x):
    return np.log(1 + x)

def sin_func(x):
    return np.sin(x)

def fourier_coefficients(func, n_terms, L):
    """Compute Fourier coefficients a0, an, and bn for a given function."""
    a0 = (1 / L) * quad(lambda x: func(x), -L, L)[0]
    an = []
    bn = []
    for n in range(1, n_terms + 1):
        an_term = (1 / L) * quad(lambda x: func(x) * np.cos(n * np.pi * x / L), -L, L)[0]
        bn_term = (1 / L) * quad(lambda x: func(x) * np.sin(n * np.pi * x / L), -L, L)[0]
        an.append(an_term)
        bn.append(bn_term)
    return a0, an, bn

def fourier_series(x, a0, an, bn, L):
    """Reconstruct the function using Fourier series."""
    result = a0 / 2
    for n in range(1, len(an) + 1):
        result += an[n - 1] * np.cos(n * np.pi * x / L) + bn[n - 1] * np.sin(n * np.pi * x / L)
    return result

def fourier_square_wave(x, terms):
    """Fourier series using numpy."""
    n = np.arange(1, terms + 1, 2)  # Odd harmonics
    return np.sum((4 / (np.pi * n)) * np.sin(n * x[:, np.newaxis]), axis=1)

x_values_square = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
x_values_exp = np.linspace(-6, 6, 1000)
x_values_ln = np.linspace(-1, 1, 1000)
x_values_sin = np.linspace(-6, 6, 1000)

y_values = []
y_exp = []
y_ln = []
y_sin = []

# Approximate Square Wave using Fourier series
start_square = time.time()
for i in range(3):
    y_values.append(fourier_square_wave(x_values_square, terms=5*(i+1)))
end_square = time.time()
print(f"Square wave execution time: {end_square - start_square:.6f} seconds")

# Approximate e^x using Fourier series
start_exp = time.time()
for i in range(3):
    a0_exp, an_exp, bn_exp = fourier_coefficients(exp_func, n_terms=5*(i+1), L=6)
    y_exp.append([fourier_series(x, a0_exp, an_exp, bn_exp, L=6) for x in x_values_exp])
end_exp = time.time()
print(f"e^x execution time: {end_exp - start_exp:.6f} seconds")

# Approximate ln(1+x) using Fourier series
start_ln = time.time()
for i in range(3):
    a0_ln, an_ln, bn_ln = fourier_coefficients(ln_func, n_terms=5*(i+1), L=1)
    y_ln.append([fourier_series(x, a0_ln, an_ln, bn_ln, L=1) for x in x_values_ln])
end_ln = time.time()
print(f"ln(1+x) execution time: {end_ln - start_ln:.6f} seconds")

# Approximate sinx(x) using Fourier series
start_sin = time.time()
for i in range(3):
    a0_sin, an_sin, bn_sin = fourier_coefficients(sin_func, n_terms=i+1, L=np.pi)
    y_sin.append([fourier_series(x, a0_sin, an_sin, bn_sin, L=np.pi) for x in x_values_sin])
end_sin = time.time()
print(f"sin(x) execution time: {end_sin - start_sin:.6f} seconds")

# Plot the results
plt.figure(figsize=(18, 6))

# Plot square wave approximation
plt.subplot(2, 2, 1)
for i in range(3):
    plt.plot(x_values_square, y_values[i], label=f"Série de Fourier (n = {5 * (i + 1)})")
plt.title("Aproximação de uma onda quadrada pela Série de Fourier")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid()

# Plot e^x approximation
plt.subplot(2, 2, 2)
plt.plot(x_values_exp, exp_func(x_values_exp), label="e^x")
for i in range(3):
    plt.plot(x_values_exp, y_exp[i], label=f"Série de Fourier (n = {5 * (i + 1)})")
plt.title("Aproximação de e^x pela Série de Fourier")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid()

# Plot ln(1+x) approximation
plt.subplot(2, 2, 3)
plt.plot(x_values_ln, ln_func(x_values_ln), label="ln(1+x)")
for i in range(3):
    plt.plot(x_values_ln, y_ln[i], label=f"Série de Fourier (n = {5 * (i + 1)})")
plt.title("Aproximação de ln(1+x) pela Série de Fourier")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid()

# Plot sin(x) approximation
plt.subplot(2, 2, 4)
plt.plot(x_values_sin, sin_func(x_values_sin), label="sin(x)", color="black", linestyle="--", linewidth=2)
for i in range(3):
    plt.plot(x_values_sin, y_sin[i], label=f"Série de Fourier (n = {i + 1})")
plt.title("Aproximação de sin(x) pela Série de Fourier")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()