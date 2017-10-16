"""
Recursively calculate the factorial of 
a number.
"""

def calc_factorial(n):

    # Base case
    if n == 1:
        return n

    else:
        return n * calc_factorial(n-1)
