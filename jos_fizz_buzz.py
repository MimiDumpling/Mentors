"""
fizz buzz
"""

def fizz_buzz(n):

    for num in range(1, n+1):
        result = " "
        
        if num % 3 == 0:
            result += "fizz"

        if num % 5 == 0:
            result += "buzz"

        if result == " ":
            result += str(num)

        print result

fizz_buzz(15)

