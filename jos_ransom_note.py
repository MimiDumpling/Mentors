from collections import defaultdict

"""
Ransom Note:

- string1 is the ransom you want to write
- string2 is the magazine you have to cut out the letters (or words -- this is harder)
- return True if there's enough magazine letters/words
- else: False

THIS SOLUTION SOLVES FOR LETTERS
"""

# more meaningful parameters
def ransom(ransom, magazine):

    available = defaultdict(int)

    if len(ransom) > len(magazine):
        return False

    for letter in magazine:
        # Look into default dict
        available[letter] += 1
    
    for letter in ransom:
        if available[letter] < 0:
            return False

        if letter in available:
            available[letter] -= 1
        else:
            return False

    print available
    return True


# write more tests
print ransom("cat", "hat")
# print ransom ("Oh hi.", "car")
# print ransom (" ", " ")
# print ransom ("Hi", "")
# print ransom ("Hi", " ")
