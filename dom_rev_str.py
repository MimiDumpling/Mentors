"""
Write a function that reverses a string.
Use as much memory as you want.
"""

def reverse_str(string):

    lst = list(string)

    current = len(lst) - 1

    new_lst = []

    while current > -1:
        new_lst.append(lst[current])
        current -= 1
        #print new_lst

    return "".join(new_lst)

print reverse_str("cat")
print reverse_str("my cat")
print reverse_str(" ")
print reverse_str("")
print reverse_str("123")
