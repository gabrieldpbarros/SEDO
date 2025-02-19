# Exemplo do termo exponencial e^x
import math
from decimal import Decimal, ROUND_DOWN

def maclaurin_exp(x, terms=10):
    """Approximate e^x using Maclaurin series."""
    result = 0.0
    for n in range(terms):
        result += (x**n) / math.factorial(n)
    return result

# Example usage
x = int(input())
mac = maclaurin_exp(x)
exp = math.exp(x)
difference = Decimal(exp - mac)

print(f"Maclaurin approximation of e^{x}: {mac}")
print(f"Exact value of e^{x}: {math.exp(x)}")
print(f"Margin of error: {difference.quantize(Decimal("0.00000000000001"), rounding=ROUND_DOWN)}")