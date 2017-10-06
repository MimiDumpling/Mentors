""" Implement merge sort. 
Merge sort takes two lists (sorted or unsorted), merges
the lists and sorts them.

Examples:
    
    # odds and evens, length even
    >>> merge_sort([1, 3, 5, 2, 4, 6])
    [1, 2, 3, 4, 5, 6]

    # already sorted, length odd
    >>> merge_sort([2, 3, 4])
    [2, 3, 4]

    # one num off, length even
    >>> merge_sort([3, 1, 2, 4, 5, 6])
    [1, 2, 3, 4, 5, 6]

    # one num, length odd
    >>> merge_sort([1])
    [1]

"""
import sys

def merge_sort(lst):
    """Merge sort list --break into pieces-- and return result."""

    print "HIYA lst: ", lst

    # Base Case
    # Break everything down into a list of one
    if len(lst) < 2:  # if length of lst is 1, return lst
        return lst

    # QUESTION: WHAT PROBS INTUITIVELY NEED TO BE HALVED??
    mid = int(len(lst) / 2)  # index at half the list
    lst1 = merge_sort(lst[:mid])  # divide list in half
    lst2 = merge_sort(lst[mid:])  # assign other half

    print "SUP lst1: ", lst1
    print "SUP lst2: ", lst2

    return make_merge(lst1, lst2)
 

def make_merge(lst1, lst2):
    """Merge two lists."""

    result = []
    index1 = 0
    index2 = 0

    print "FOO lst1: ", lst1
    print "FOO lst2: ", lst2

    while index1 < len(lst1) and index2 < len(lst2):
        print "\tlength lst1: ", len(lst1), "index1: ", index1
        sys.stdout.flush()
        # print "LOOP lst1: ", lst1
        # print "LOOP lst2: ", lst2
        if lst1[index1] < lst2[index2]:
            result.append(lst1[index1])
            index1 += 1
        else:
            result.append(lst2[index2])
            index2 += 1

    if index1 < len(lst1):
        result.extend(lst1[index1:])

    if index2 < len(lst2):
        result.extend(lst2[index2:])

    return result





if __name__ == '__main__':
    print merge_sort([1, 3, 5, 2, 4, 6])
