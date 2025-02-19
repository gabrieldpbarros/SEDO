import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("fourier_data.txt")
x = data[:, 0]
y = data[:, 1]

plt.plot(x, y, label="Fourier Approximation")
plt.title("Fourier Series Approximation of a Square Wave")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid()
plt.show()