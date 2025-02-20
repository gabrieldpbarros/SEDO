import numpy as np
from scipy.integrate import quad

# Função original
def exp_func(x):
    return np.exp(x)

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
L = 1  # Intervalo [-L, L] para a série de Fourier
n_terms = 9  # Número de parcelas (termos) na série de Fourier
x_target = 1  # Ponto onde queremos avaliar a aproximação

# Calcular os coeficientes de Fourier
a0, an, bn = fourier_coefficients_exp(n_terms, L)

# Avaliar a série de Fourier em x = 1
approx_value = fourier_series_exp(x_target, a0, an, bn, L)

# Valor exato de e^1
exact_value = np.exp(x_target)

# Calcular o erro absoluto
error = np.abs(exact_value - approx_value)

# Exibir resultados
print(f"Aproximação de e^{x_target} usando {n_terms} parcelas da série de Fourier: {approx_value:.6f}")
print(f"Valor exato de e^{x_target}: {exact_value:.6f}")
print(f"Erro absoluto: {error:.6f}")