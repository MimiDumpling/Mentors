"""
Implement a class. Maintains a sorted list.
methods:
    insert - add a new num
    lowest - lowest num
    highest - highest num

"""

class SortedList(object):
    " "

    def __init__(self):
        self.lst = []

    def insert(self, num):
        initial_len = len(self.lst)

        for i in range(0, len(self.lst)):
            if num < self.lst[i]:
                self.lst.insert(i, num)
                break

        if initial_len == len(self.lst):
            self.lst.append(num)

    def lowest(self):
        if self.lst:
            return self.lst[0]
        else:
            return None

    def highest(self):
        if self.lst:
            return self.lst[-1]
        else:
            return None



sl = SortedList()
print sl.lowest()


