import time
import numpy as np

def sin_func(x):
    return np.sin(x)

x_values = np.linspace(-6, 6, 1000)
start = time.time()
sin_func(x_values)
end = time.time()

print(f"Tempo de execucao: {end - start:.6f} segundos")