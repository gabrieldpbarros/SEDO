import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import time

def exp_func(x):
    return np.exp(x)

def ln_func(x):
    return np.log(1 + x)

def fourier_coefficients(func, n_terms, L=1):
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

def fourier_series(x, a0, an, bn, L=1):
    """Reconstruct the function using Fourier series."""
    result = a0 / 2
    for n in range(1, len(an) + 1):
        result += an[n - 1] * np.cos(n * np.pi * x / L) + bn[n - 1] * np.sin(n * np.pi * x / L)
    return result

def fourier_square_wave_optimized(x, terms):
    """Optimized Fourier series using numpy."""
    n = np.arange(1, terms + 1, 2)  # Odd harmonics
    return np.sum((4 / (np.pi * n)) * np.sin(n * x[:, np.newaxis]), axis=1)

# min = 5, max = 25
y_values = []
y_exp = []
y_ln = []

# square wave
x_values_square = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
start_square = time.time()
for i in range(3):
    y_values.append(fourier_square_wave_optimized(x_values_square, terms=5*(i+1)))
end_square = time.time()
print(f"Square wave execution time: {end_square - start_square:.6f} seconds")

x_values = np.linspace(-1, 1, 1000)
# e^x
start_exp = time.time()
for i in range(3):
    a0_exp, an_exp, bn_exp = fourier_coefficients(exp_func, n_terms=5*(i+1))
    y_exp.append([fourier_series(x, a0_exp, an_exp, bn_exp) for x in x_values])
end_exp = time.time()
print(f"e^x execution time: {end_exp - start_exp:.6f} seconds")

# ln(1+x)
start_ln = time.time()
for i in range(3):
    a0_ln, an_ln, bn_ln = fourier_coefficients(ln_func, n_terms=5*(i+1))
    y_ln.append([fourier_series(x, a0_ln, an_ln, bn_ln) for x in x_values])
end_ln = time.time()
print(f"ln(1+x) execution time: {end_ln - start_ln:.6f} seconds")

# Plot the results
plt.figure(figsize=(18, 6))

# Plot square wave approximation
plt.subplot(1, 3, 1)
for i in range(3):
    plt.plot(x_values_square, y_values[i], label=f"Série de Fourier para qt.termos = {5 * (i + 1)}")
plt.title("Aproximação de uma onda quadrada pela Série de Fourier")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid()

# Plot e^x approximation
plt.subplot(1, 3, 2)
plt.plot(x_values, exp_func(x_values), label="e^x")
for i in range(3):
    plt.plot(x_values, y_exp[i], label=f"Série de Fourier para qt.termos = {5 * (i + 1)}")
plt.title("Aproximação de e^x pela Série de Fourier")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid()

# Plot ln(1+x) approximation
plt.subplot(1, 3, 3)
plt.plot(x_values, ln_func(x_values), label="ln(1+x)")
for i in range(3):
    plt.plot(x_values, y_ln[i], label=f"Série de Fourier para qt.termos = {5 * (i + 1)}")
plt.title("Aproximação de ln(1+x) pela Série de Fourier")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()