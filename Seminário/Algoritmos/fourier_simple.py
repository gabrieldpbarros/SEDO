# Exemplo de uma onda quadrada
import numpy as np
import matplotlib.pyplot as plt

def fourier_square_wave(x, terms=10):
    """Approximate a square wave using Fourier series."""
    result = 0.0
    for n in range(1, terms + 1, 2):  # Only odd harmonics
        result += (4 / (np.pi * n)) * np.sin(n * x)
    return result

# Generate data
x_values = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
y_values = [fourier_square_wave(x, terms=10) for x in x_values]

# Plot
plt.plot(x_values, y_values, label="Fourier Approximation")
plt.title("Fourier Series Approximation of a Square Wave")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid()
plt.show()