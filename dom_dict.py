import time

"""

Write a class that does this:
.set_key('cat', 'Pan')
.get_value('cat')
=> 'Pan'

.set_key('cat', 'Pan')
.get_value('cat', 1)
=> 'Pan'

.set_key('cat', 'Maple')
.get_value('cat', 2)
=> 'Maple'

.get_value('cat')
=> 'Maple'
"""

class HashMap(object):

    hash_map = {}
        
    def set_key(self, key, value):
        time_stamp = time.time()

        if self.hash_map.get(key):
            self.hash_map[key][time_stamp] = value

        else:
            self.hash_map[key] = {}
            self.hash_map[key][time_stamp] = value

        self.hash_map[key]["recent"] = value

        return time_stamp


    def get_value(self, key, time=None):

        if self.hash_map.get(key) == None:
            return "Sorry, that key doesn't exist."

        if time == None:
            return self.hash_map[key]["recent"]

        if self.hash_map.get(key).get(time) == None:
            return "Nope."
        
        return self.hash_map[key][time]



ready = HashMap()
now = ready.set_key('cat', 'Pan')
print ready.get_value('cat', now)

now1 = ready.set_key('cat', 'Maple')
print ready.get_value('cat', now1)

print ready.get_value('cat', now)

print ready.get_value('cat')

print ready.get_value('cat', 4)

# ready.set_key('dog', 'Max')
print ready.get_value('dog')
