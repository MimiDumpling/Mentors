from collections import defaultdict

"""
Ransom Note:

- string1 is the ransom you want to write
- string2 is the magazine you have to cut out the letters (or words -- this is harder)
- return True if there's enough magazine letters/words
- else: False

THIS SOLUTION SOLVES FOR LETTERS
"""

def ransom(ransom, magazine):

    available = defaultdict(int)

    if len(ransom) > len(magazine):
        return False

    for letter in ransom:
        available[letter] += 1
        
    #print "dict for just ransom: ", available

    for letter in magazine:
        if available[letter]:
            available[letter] -= 1

    #print "dict after magazine search: ", available

    for letter in ransom:
        if available[letter] > 0:
            return False

    return True

print "+++TESTS+++"
print "1. Correct: False, Result: ", ransom("cat", "car")
print "2. Correct: False, Result: ", ransom("Oh", "car")
print "3. Correct: False, Result: ", ransom("Hello", "yo")
print "4. Correct: False, Result: ", ransom("Hi", "")
print "5. Correct: False, Result: ", ransom("Hi", " ")
print "6. Correct: True, Result: ", ransom(" ", " ")
print "7. Correct: True, Result: ", ransom("Meow", "Meow")
print "8. Correct: False, Result: ", ransom("Meoow", "Meowwwww")
# why doesn't "w" register as a neg num when we print dict?

