from collections import defaultdict

"""
String compression.
collapse down repeated sequence of letters.
only compress more than 2 repeats
Take a string. break into list.
#1 implement compression into new copy.
#2 implement in place

Ex)
"aaaa" => a4

# doesn't compress only 2 repeats
"aabbb" => aab3

"""

def str_compression(string):
    lowered_string = string.lower()
    repeats = defaultdict(int)
    # maybe check each word separately and then .join later
    words = string.split(" ")

    if len(string) < 3:
        return string

    for index, char in enumerate(string):
        # if char == " ":
        # need to account for spaces/new words "kitttty cat"
        repeats[char] += 1

    new_string = ""
    # how can we skip to the next char that isn't repeated?
    # do we alter lowered_string by slicing??
    for char in lowered_string:
        if repeats[char] > 2:
            new_string += (char + str(repeats[char]))
        else:
            new_string += char

    return new_string

# similar to merge sort. have 2 runners. input runner, output runner.


print str_compression("kitttty")
print str_compression("kitty")
print str_compression("kitttty       catttt")
print str_compression(" ")


