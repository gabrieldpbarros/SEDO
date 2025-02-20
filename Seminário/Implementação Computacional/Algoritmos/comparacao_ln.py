import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.special import factorial

# Função original
def ln_func(x):
    return np.log(1 + x)

# Série de Maclaurin para ln(1+x)
def maclaurin_ln(x, terms):
    """Aproximação de ln(1+x) usando a série de Maclaurin."""
    n = np.arange(1, terms + 1)
    return np.sum(((-1)**(n + 1)) * (x[:, np.newaxis]**n) / n, axis=1)

# Coeficientes da série de Fourier para ln(1+x)
def fourier_coefficients_ln(n_terms, L):
    """Calcula os coeficientes de Fourier para ln(1+x)."""
    a0 = (1 / L) * quad(lambda x: ln_func(x), -L, L)[0]
    an = []
    bn = []
    for n in range(1, n_terms + 1):
        an_term = (1 / L) * quad(lambda x: ln_func(x) * np.cos(n * np.pi * x / L), -L, L)[0]
        bn_term = (1 / L) * quad(lambda x: ln_func(x) * np.sin(n * np.pi * x / L), -L, L)[0]
        an.append(an_term)
        bn.append(bn_term)
    return a0, an, bn

# Série de Fourier para ln(1+x)
def fourier_series_ln(x, a0, an, bn, L):
    """Aproximação de ln(1+x) usando a série de Fourier."""
    result = a0 / 2
    for n in range(1, len(an) + 1):
        result += an[n - 1] * np.cos(n * np.pi * x / L) + bn[n - 1] * np.sin(n * np.pi * x / L)
    return result

# Parâmetros
L = 1  # Intervalo [-L, L] para a série de Fourier
n_values = [5, 10, 15]  # Número de termos nas séries
x_values_ln = np.linspace(-0.99, 1, 1000)  # Pontos para avaliação de ln(1+x)

# Função para plotar as comparações para ln(1+x)
def plot_comparison_ln():
    plt.figure(figsize=(18, 6))
    for i, n in enumerate(n_values):
        # Aproximação de Maclaurin
        y_maclaurin = maclaurin_ln(x_values_ln, n)
        
        # Aproximação de Fourier
        a0, an, bn = fourier_coefficients_ln(n, L)
        y_fourier = fourier_series_ln(x_values_ln, a0, an, bn, L)
        
        # Plotar os resultados
        plt.subplot(1, 3, i + 1)
        plt.plot(x_values_ln, ln_func(x_values_ln), label="Função Original", color="black", linewidth=2, linestyle="--")
        plt.plot(x_values_ln, y_maclaurin, label="Série de Maclaurin")
        plt.plot(x_values_ln, y_fourier, label="Série de Fourier")
        plt.title(f"Aproximação de ln(1+x) (n = {n})")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.legend()
        plt.grid()
    plt.tight_layout()
    plt.show()

# Plotar comparações para ln(1+x)
plot_comparison_ln()