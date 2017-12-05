"""
Implement .split() without using .split().

Edge cases to keep in mind:
 1) " " is not ""
 2) "hey    you" (multiple spaces)
    ["hey", "you"]
 3) "sup" (end and see no char)
    ["sup"]
"""

def split_me(char, string):

    result = []

    last_seen = -1

    for index, x in enumerate(string):
        if x == char:
            result.append(string[(last_seen + 1):index])

            last_seen = index

    result.append(string[last_seen:])

    return result

print "Test 1: ", split_me(" ", "hi there")
