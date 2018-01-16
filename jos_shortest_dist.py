import sys

"""
Given an unsorted list of integers, find the 
two integers with the lowest difference between
their values. Return the difference of those
two integers.

BONUS: solve for 2 unsorted lists
"""

def short_dist(integers):

    lst = sorted(integers)
    diff = sys.maxsize

    for index, n in enumerate(lst):
        if index < len(lst) - 1:
            x = lst[index + 1] - n
            if x < diff:
                diff = x

    return diff

print "+++TESTS+++"
print "Correct Answer: 1, Result: ", short_dist([47, 1, 12, 48, 9, 23])
print "Correct Answer: 3, Result: ", short_dist([1, 4, 100])
print "Correct Answer: 2, Result: ", short_dist([2, 0])

