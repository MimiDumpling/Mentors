from collections import defaultdict

"""
Ransom Note:

- string1 is the ransom you want to write
- string2 is the magazine you have to cut out the letters (or words -- this is harder)
- return True if there's enough magazine letters/words
- else: False

THIS SOLUTION SOLVES FOR WORDS
"""

def ransom(ransom, magazine):

    split_ransom = ransom.split(" ")
    split_magazine = magazine.split(" ")
    available = defaultdict(int)

    if len(ransom) > len(magazine):
        return False

    for word in split_ransom:
        # Look into default dict
        available[word] += 1
    
    for word in split_magazine:
        if available[word]:
            available[word] -= 1

    for word in split_ransom:
        if available[word] > 0:
            return False

    return True

print "+++TESTS+++"
print "1. Correct: False, Result: ", ransom("cat in car", "cat in box")
print "2. Correct: False, Result: ", ransom("Oh", "car")
print "3. Correct: False, Result: ", ransom("Hello", "Hello you")
print "4. Correct: False, Result: ", ransom("Hi", "")
print "5. Correct: False, Result: ", ransom("Hi", " ")
print "6. Correct: True, Result: ", ransom(" ", " ")
print "7. Correct: True, Result: ", ransom("Meow meow", "Meow meow")

