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

    if char == "":
        raise ValueError("Split argument must not be empty.")

    for index, x in enumerate(string):
        if x == char and last_seen + 1 != index:
            result.append(string[(last_seen + 1):index])
            last_seen = index

    if result == []:
        result.append(string)
        return result
    else:
        result.append(string[last_seen + 1:])
        return result

print "Test 1: ", split_me(" ", "")
print "Test 2: ", split_me(" ", "hey")
print "Test 3: ", split_me(" ", "hey there")
print "Test 4: ", split_me(" ", "hey there, you")
print "Test 5: ", split_me(" ", "hey       there")
print "Test 6: ", split_me("e", "hey there")
print "Test 7: ", split_me("", "hey       there")





