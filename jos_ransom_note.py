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
def ransom(string1, string2):

    note = defaultdict(int)

    for letter in string1:
        # Look into default dict
        note[letter] += 1
        

    for letter in string2:
        # WARNING: this applies to letters we aren't even focusing on
        if note.get(letter) == 0:
            return False

        if letter in note:
            note[letter] -= 1  
        # WARNING    
        else:
            return False

    return True

# write more tests
print ransom("The cat is here.", "The cat is near.")
