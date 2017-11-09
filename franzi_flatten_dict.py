"""
Given a dictionary with sub dictionaries,
create a new dictionary without sub
dictionaries but still containing the 
values from the original dict. Keys
representing values that were original in
sub dictionaries should contain the original
path as their name. For example:

original_dict = {
    'a': 4,
    'b': {
        'c': 5,
        'd': {
            'e': 6
        }
    }
}

new_dict = {
    'a': 4,
    'b.c': 5,
    'b.d.e': 6
}
"""


n = {
  'a': 5,
  'b': 6,
  'c': {
    'f': 9,
    'g': {
      'm': 17,
      'n': 3
    }
  }
}


def flat(n, flattend={}, path=""):

    # def f(d):
    print flattend

    for item in n:
        if type(n[item]) is dict:
            if path == "":
                # path = item
                flat(n[item], flattend, item)
            else:
                new_path = path + "." + item
                flat(n[item], flattend, new_path)
        else:
            if path == "":
                flattend[item] = n[item]
            else:
                new_path = path + "." + item
                flattend[new_path] = n[item]

    print flattend
    return flattend


print flat(n)
