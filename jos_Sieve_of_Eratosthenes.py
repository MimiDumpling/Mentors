"""
Implement the Sieve of Eratosthenes.
Finds all prime numbers up to given limit.
Iteratively marking as composite (i.e., not prime)
the multiples of each prime, starting 
with the first prime number, 2. The multiples 
of a given prime are generated as a sequence 
of numbers starting from that prime, with 
constant difference between them that is 
equal to that prime.

So, find prime num (2) and find all 
multiples of it within the limit (or max).
Eliminate all multiples of this prime num.
Do this to all prime nums until there are 
no other prime nums that have multiples. 

Print out the remaining nums, which should
all be prime between 2 - limit (or max).
"""

def is_prime(num):
    
    if num == 2:
        return True

    for potential_divider in range(2, num):
        if num % potential_divider == 0:
            return False
    return True



def print_prime(max):

    numbers = range(2, max)

    for potential_prime in numbers:
        if is_prime(potential_prime):
            for i in range((potential_prime*potential_prime), max, potential_prime):
                numbers.pop(i)
                print "+++++++++"
                print numbers

    print "********"
    print numbers


# def print_prime(max):

#     for potential_prime in range (2, max):
#         if is_prime(potential_prime):
#             print potential_prime





print_prime(15)



