# Exemplo do termo exponencial e^x
import numpy as np
import time

def maclaurin_exp_optimized(x, terms=10):
    """Optimized Maclaurin series using numpy."""
    n = np.arange(terms)
    return np.sum((x**n) / np.math.factorial(n))

# Example usage
x = int(input("Digite o valor de x: "))

start = time.time()
mac = maclaurin_exp_optimized(x)
end = time.time()

print(f"Optimized Maclaurin approximation of e^{x}: {maclaurin_exp_optimized(x)}")
print(f"Execution time: {(end - start):.6f} seconds")