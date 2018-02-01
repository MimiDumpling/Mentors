"""

Write a class that does this:
.set('cat', 'Pan')
.get('cat')
=> 'Pan'

"""
from collections import defaultdict


class HashMap(object):
    
    def __init__(self, animal, name):

        self.animal = animal
        self.name = name

    def set(self, animal, name):

        hashmap = defaultdict(list)

        hashmap[self.animal].append(self.name)

    def get(self, animal):

        print hashmap[self.animal]


ready = HashMap(cat, Pan)
ready.set(cat, Pan)
ready.set(dog, Max)
