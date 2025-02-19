# Exemplo de uma onda quadrada
import numpy as np
import matplotlib.pyplot as plt
import time

def fourier_square_wave_optimized(x, terms):
    """Optimized Fourier series using numpy."""
    n = np.arange(1, terms + 1, 2)  # Odd harmonics
    return np.sum((4 / (np.pi * n)) * np.sin(n * x[:, np.newaxis]), axis=1)

# Example usage
terms = int(input("Type the amount of terms: "))
start = time.time()
x_values = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
y_values = fourier_square_wave_optimized(x_values, terms)
end = time.time()

print(f"Execution time: {(end - start):.6f} seconds")

# Plot
plt.plot(x_values, y_values, label=f"Série de Fourier para  x = {terms}")
plt.title("Aproximação de uma onda quadrada pela Série de Fourier")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid()
plt.show()