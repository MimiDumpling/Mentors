"""
Write a binary search. Not a binary tree search.

Given a list of numbers and a number, return True
if the number is in the list or False if not. Do
this as a binary search -- divide and conquer.

"""

def binary_search(lst, num):

    start = 0
    end = len(lst)

    while True:
        mid = start + (end-start)/2

        if lst[mid] == num:
            return True

        if lst[mid] < num:
            start = mid
        else:
            end = mid

        if start + (end-start) == mid:
            return False
        
