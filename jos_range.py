"""
Say you're working on a program that deals with input strings 
of a certain form. The input strings are supposed to be 
comma-separated single characters: so for example, a valid 
input would be "a,b,c,d,e,q" but an invalid input would 
be "abc,def" (because there isn't a comma in between every 
    character). Keep in mind, the input is not a list - it's a 
string that kinda LOOKS like a list :)
You want to write a syntax checker function that takes a 
string and returns True if it's valid and False if it's invalid, 
by making sure that every other character in the string is a 
comma (that's the only check it needs to perform). For this one, 
you might want to re-read the documentation for range() and pay 
attention to the optional "step" parameter.
"""


def syntax_chkr(string):

    if string == "" or string == " ":
        return False

    for index in range(1, len(string), 2):
        if string[index] is not ",":
            return False

    return True


print syntax_chkr("a,b,c")
print syntax_chkr("a, bc")
print syntax_chkr("")
print syntax_chkr(" ")
