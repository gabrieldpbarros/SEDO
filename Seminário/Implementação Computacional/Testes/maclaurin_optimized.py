# Exemplo do termo exponencial e^x
import numpy as np

def maclaurin_exp_optimized(x, terms=10):
    """Optimized Maclaurin series using numpy."""
    n = np.arange(terms)
    return np.sum((x**n) / np.math.factorial(n))

# Example usage
x = 2.0
print(f"Optimized Maclaurin approximation of e^{x}: {maclaurin_exp_optimized(x)}")