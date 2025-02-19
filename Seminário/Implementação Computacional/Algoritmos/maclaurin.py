import numpy as np
from scipy.special import factorial
import time

def maclaurin_exp_optimized(x, terms):
    """Optimized Maclaurin series using numpy."""
    n = np.arange(terms)
    return np.sum((x**n) / factorial(n))