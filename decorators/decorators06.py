"""
Example 06
"""
import math
from decorators import debug

math.factorial = debug(math.factorial)

def approximate_e(terms=18):
    """Apply a decorator to a standard library function"""
    return sum(1 / math.factorial(n) for n in range(terms))

print(approximate_e(5))
