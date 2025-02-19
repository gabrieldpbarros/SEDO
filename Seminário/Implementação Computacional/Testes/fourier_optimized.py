# Exemplo de uma onda quadrada
import numpy as np
import matplotlib.pyplot as plt

def fourier_square_wave_optimized(x, terms=10):
    """Optimized Fourier series using numpy."""
    n = np.arange(1, terms + 1, 2)  # Odd harmonics
    return np.sum((4 / (np.pi * n)) * np.sin(n * x[:, np.newaxis]), axis=1)

# Example usage
x_values = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
y_values = fourier_square_wave_optimized(x_values, terms=10)

# Plot
plt.plot(x_values, y_values, label="Optimized Fourier Approximation")
plt.title("Optimized Fourier Series Approximation of a Square Wave")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid()
plt.show()