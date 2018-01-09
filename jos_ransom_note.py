"""
Ransom Note:

- string1 is the ransom you want to write
- string2 is the magazine you have to cut out the letters (or words -- this is harder)
- return True if there's enough magazine letters/words
- else: False

THIS SOLUTION SOLVES FOR LETTERS
"""

def ransom(string1, string2):

    note = {}

    for letter in string1:
        if letter in note:
            note[letter] += 1
        else:
            note[letter] = 1

    for letter in string2:
        if note.get(letter) == 0:
            return False

        if letter in note:
            note[letter] -= 1  
        else:
            return False

    return True


print ransom("The cat is here.", "The cat is near.")
