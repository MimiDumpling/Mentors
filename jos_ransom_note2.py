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

    if len(ransom) > len(magazine):
        return False

    split_ransom = ransom.split(" ")
    split_magazine = magazine.split(" ")
    note = defaultdict(int)

    for word in split_magazine:
        note[word] += 1

    print split_magazine
    print note

    for word in split_ransom:
        if note[word] < 0:
            return False
    print note

    # #print "First note: ", note

    # for word in split_ransom:
    #     if word not in note:
    #         print False
    #     else:
    #         note[word] -= 1

    #     if note[word] < 0:
    #         return False

    #     # if note[word] < 0:
    #         #return False

    #     # if word in note:
    #     #     note[word] -= 1
    #     # else:
    #     #     return False

    # print note
    # return True

print "++++++++++++++++++++++++++++"
print ransom("My", "Cat")
# print ransom("cat hat", "cat has")
# print ransom(" ", " ")
# print ransom("Hi", "Hello")
# print ransom("race car", "race car")
# print ransom("", " ")
# print ransom("Hey", " ")

dictionary.items()






