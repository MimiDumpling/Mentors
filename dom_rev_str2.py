"""
Write a function that reverses a string.
Do it in place.
"""

def reverse_str(string):

    if string == "":
        return ""

    lst = list(string)
    current = len(lst)-1

    for index in range(0,len(lst)):

        if index >= current:
            return "".join(lst)

        temp = lst[index]
        lst[index] = lst[current]
        lst[current] = temp

        index += 1
        current -= 1

print reverse_str("cat")
print reverse_str("my cat")
print reverse_str(" ")
print reverse_str("")
print reverse_str("123")
