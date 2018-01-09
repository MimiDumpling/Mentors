"""
Ransom Note:

- string1 is the ransom you want to write
- string2 is the magazine you have to cut out the letters (or words -- this is harder)
- return True if there's enough magazine letters/words
- else: False

THIS SOLUTION SOLVES FOR WORDS
"""

def ransom(string1, string2):

    split_string1 = string1.split(" ")
    split_string2 = string2.split(" ")
    note = {}

    if len(split_string1) != len(split_string2):
        return False

    for word in split_string1:
        if word in note:
            note[word] += 1
        else:
            note[word] = 1

    for word in split_string2:
        if note.get(word) == 0:
            return False

        if word in note:
            note[word] -= 1
        else: 
            return False

    return True

print ransom("cat hat", "cat has")
