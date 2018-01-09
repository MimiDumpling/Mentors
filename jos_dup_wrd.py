"""
- takes a word
- return true if all letters are unique
- false if duplicate letters
"""

def dups(word):

    letters = {}
    word = word.lower()

    for letter in word:
        if letter in letters:
            return False, "BOOOO" 

        else:
            letters[letter] = 1

    return True, "HAY"

result, msg = dups("Ss")
print result, msg


"""
Ransom Note:

- string1 is the ransom you want to write
- string2 is the magazine you have to cut out the letters (or words -- this is harder)
- return True if there's enough magazine letters/words
- else: False
"""
