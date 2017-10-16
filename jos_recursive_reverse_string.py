"""
Recursively reverse a string.
"""

def reverse_string(str):

    # Base Case
    if len(str) == 1:
        return str
    else:
        return reverse_string(str[1:]) + str[0]
