import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.special import factorial

# Função original
def exp_func(x):
    return np.exp(x)

# Série de Maclaurin para e^x (otimizada)
def maclaurin_exp(x, terms):
    """Aproximação de e^x usando a série de Maclaurin."""
    n = np.arange(terms)
    return np.sum((x[:, np.newaxis]**n) / factorial(n), axis=1)

# Coeficientes da série de Fourier para e^x
def fourier_coefficients_exp(n_terms, L):
    """Calcula os coeficientes de Fourier para e^x."""
    a0 = (1 / L) * quad(lambda x: exp_func(x), -L, L)[0]
    an = []
    bn = []
    for n in range(1, n_terms + 1):
        an_term = (1 / L) * quad(lambda x: exp_func(x) * np.cos(n * np.pi * x / L), -L, L)[0]
        bn_term = (1 / L) * quad(lambda x: exp_func(x) * np.sin(n * np.pi * x / L), -L, L)[0]
        an.append(an_term)
        bn.append(bn_term)
    return a0, an, bn

# Série de Fourier para e^x
def fourier_series_exp(x, a0, an, bn, L):
    """Aproximação de e^x usando a série de Fourier."""
    result = a0 / 2
    for n in range(1, len(an) + 1):
        result += an[n - 1] * np.cos(n * np.pi * x / L) + bn[n - 1] * np.sin(n * np.pi * x / L)
    return result

# Parâmetros
L = 6  # Intervalo [-L, L] para a série de Fourier
n_values = [5, 10, 15]  # Número de termos nas séries
x_values_exp = np.linspace(-L, L, 1000)  # Pontos para avaliação de e^x

# Função para plotar as comparações para e^x
def plot_comparison_exp():
    plt.figure(figsize=(18, 6))
    for i, n in enumerate(n_values):
        # Aproximação de Maclaurin
        y_maclaurin = maclaurin_exp(x_values_exp, n)
        
        # Aproximação de Fourier
        a0, an, bn = fourier_coefficients_exp(n, L)
        y_fourier = fourier_series_exp(x_values_exp, a0, an, bn, L)
        
        # Plotar os resultados
        plt.subplot(1, 3, i + 1)
        plt.plot(x_values_exp, exp_func(x_values_exp), label="Função Original", color="black", linewidth=2, linestyle="--")
        plt.plot(x_values_exp, y_maclaurin, label=f"Série de Maclaurin (n = {n})")
        plt.plot(x_values_exp, y_fourier, label=f"Série de Fourier (n = {n})")
        plt.title(f"Aproximação de e^x (n = {n})")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.legend()
        plt.grid()
    plt.tight_layout()
    plt.show()

# Plotar comparações para e^x
plot_comparison_exp()