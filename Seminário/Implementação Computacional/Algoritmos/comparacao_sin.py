import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.special import factorial

# Função original
def sin_func(x):
    return np.sin(x)

# Série de Maclaurin para sin(x)
def maclaurin_sin(x, terms):
    """Aproximação de sin(x) usando a série de Maclaurin."""
    n = np.arange(terms)
    return np.sum(((-1)**n) * (x[:, np.newaxis]**(2 * n + 1)) / factorial(2 * n + 1), axis=1)

# Coeficientes da série de Fourier para sin(x)
def fourier_coefficients_sin(n_terms, L):
    """Calcula os coeficientes de Fourier para sin(x)."""
    an = []
    bn = []
    for n in range(1, n_terms + 1):
        an_term = (1 / L) * quad(lambda x: sin_func(x) * np.cos(n * np.pi * x / L), -L, L)[0]
        bn_term = (1 / L) * quad(lambda x: sin_func(x) * np.sin(n * np.pi * x / L), -L, L)[0]
        an.append(an_term)
        bn.append(bn_term)
    return an, bn

# Série de Fourier para sin(x)
def fourier_series_sin(x, an, bn, L):
    """Aproximação de sin(x) usando a série de Fourier."""
    result = np.zeros_like(x)  # a0 = 0 para sin(x), então não precisamos adicioná-lo
    for n in range(1, len(an) + 1):
        result += an[n - 1] * np.cos(n * np.pi * x / L) + bn[n - 1] * np.sin(n * np.pi * x / L)
    return result

# Parâmetros
L = np.pi  # Melhor intervalo para sin(x)
n_values = [1, 3, 5]  # Número de termos nas séries
x_values_sin = np.linspace(-3*np.pi, 3*np.pi, 1000)  # Intervalo de plotagem

# Função para plotar a comparação para sin(x)
def plot_comparison_sin():
    plt.figure(figsize=(18, 6))

    for i, n in enumerate(n_values):
        # Aproximação de Maclaurin
        y_maclaurin = maclaurin_sin(x_values_sin, n)
        
        # Aproximação de Fourier
        an, bn = fourier_coefficients_sin(n, L)
        y_fourier = fourier_series_sin(x_values_sin, an, bn, L)
        
        # Plotar os resultados
        plt.subplot(1, 3, i + 1)
        plt.plot(x_values_sin, sin_func(x_values_sin), label="Função Original", color="black", linewidth=2, linestyle="--")
        plt.plot(x_values_sin, y_maclaurin, label="Série de Maclaurin")
        plt.plot(x_values_sin, y_fourier, label="Série de Fourier")
        plt.title(f"Aproximação de sin(x) (n = {n})")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.ylim(-2, 2)
        plt.legend()
        plt.grid()
    
    plt.tight_layout()
    plt.show()

# Plotar comparações para sin(x)
plot_comparison_sin()