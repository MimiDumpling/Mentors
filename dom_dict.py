"""

Write a class that does this:
.set('cat', 'Pan')
.get('cat')
=> 'Pan'

"""

class HashMap(object):

    hash = {}
    
    def set_key(self, key, value):
        self.hash[key] = value

    def get_value(self, key):
        return self.hash[key]

ready = HashMap()
ready.set_key('cat', 'Pan')
print ready.get_value('cat')

ready.set_key('dog', 'Max')
print ready.get_value('dog')
