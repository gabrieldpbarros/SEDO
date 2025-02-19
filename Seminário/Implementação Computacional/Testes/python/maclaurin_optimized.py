# Exemplo do termo exponencial e^x
import numpy as np
from scipy.special import factorial
import time

def maclaurin_exp_optimized(x, terms):
    """Optimized Maclaurin series using numpy."""
    n = np.arange(terms)
    return np.sum((x**n) / factorial(n))

# Example usage
x = int(input("Type x value: "))
terms = int(input("Type the amount of terms: "))

start = time.time()
mac = maclaurin_exp_optimized(x, terms)
end = time.time()

print(f"Optimized Maclaurin approximation of e^{x}: {mac}")
print(f"Execution time: {(end - start):.6f} seconds")