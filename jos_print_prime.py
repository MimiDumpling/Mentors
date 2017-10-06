"""
Write a function that takes a number
and prints all the prime integers from zero
the that number. You don't need to print 
1 and the number.

"""

def is_prime(num):
    if num == 2:
        return True

    for potential_divisor in range (2, num):
        if num % potential_divisor == 0:
            return False
    return True

def print_prime(max):
    for maybe_prime in range (2, max):
        if is_prime(maybe_prime):
            print maybe_prime


print "++++ Tests BEGIN ++++"
print "--0--"
print_prime(0)
print "--10--"
print_prime(10)
print "--5--"
print_prime(5)
print "****Tests END *****"
