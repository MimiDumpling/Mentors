# def rot4_encrypt():
#     """Encrypts a string of letters by rotating each letter four indexes in alphabet."""

#     alphabet=["a","b","c","d","e","f","g","h","i","j","k","l",
#     "m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

#     dictionary = {}

#     # range(0, 26)
#     for char in range(0, len(alphabet)):

#         dictionary[alphabet[char]] = alphabet[(char + 4)%len(alphabet)]

#     print dictionary

# rot4_encrypt()


# chr() returns a string of one character whose ASCII code is the integer i. 
# For example, chr(97) returns the string 'a'.    
LOWER_LETTERS = [chr(x) for x in range(97, 123)]
UPPER_LETTERS = [chr(x) for x in range(65, 91)]

def rot4():
    source_string = raw_input("Enter string to rot4:")
    result_string = ""
    for char in source_string:
        if char.isupper():
            result_string += encrypt(char, UPPER_LETTERS)
        elif char.islower():
            result_string += encrypt(char, LOWER_LETTERS)
        else:
            result_string += char
    print("The rot4 encrypted string is:%s" % (result_string))

    want_to_decrypt = raw_input("Do you want to decrypt? Yes or No?")

    if want_to_decrypt.lower() == "yes":
        decrypted = ""
        for char in result_string:
            if char.isupper():
                decrypted += decrypt(char, UPPER_LETTERS)
            elif char.islower():
                decrypted += decrypt(char, LOWER_LETTERS)
            else:
                decrypted += char
        print "The rot4 decrypted string is:%s" % (decrypted)
    else:
        print "Ok. No decryption. See you next time."
            

def encrypt(char, letter_list):
    result_char = ''
    # .index() returns index of char in LOWER_LETTERS or UPPER_LETTERS
    original_index = letter_list.index(char)
    new_index = original_index + 4
    # need to get remainder so we know which index to access??
    result_char += letter_list[new_index % len(letter_list)]
    return result_char

def decrypt(char, letter_list):
    result_char = ''
    original_index = letter_list.index(char)
    new_index = original_index - 4
    result_char += letter_list[new_index % len(letter_list)]
    return result_char

    

if __name__ == '__main__':
    rot4()
