"""
Recursively print reverse of a string.
"""

def rev_string(string):

    # base case
    if len(string) == 1:
        # do a thing
        print string
        return

    rev_string(string[1:])

    print string[0]

"""
take a list of nums and calc the sum of all nums
"""
