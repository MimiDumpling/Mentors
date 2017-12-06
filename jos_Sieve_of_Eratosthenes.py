"""
Implement the Sieve of Eratosthenes.
Finds all prime numbers up to given limit. Iteratively marking as composite (i.e., not prime)
the multiples of each prime, starting with the first prime number, 2. The multiples 
of a given prime are generated as a sequence of numbers starting from that prime, with 
constant difference between them that is equal to that prime.

So, find prime num (2) and find all multiples of it within the limit (or max).
Eliminate all multiples of this prime num. Do this to all prime nums until there are 
no other prime nums that have multiples. 

Print out the remaining nums, which should all be prime between 2 - limit (or max).
"""

def sieve(n):
    
    not_prime = []

    for num in range(2, n+1):
        if num not in not_prime:
            print (num)
            for other_num in range(num*num, n+1, num):
                not_prime.append(other_num)

    print not_prime

print "this is test: ", sieve(13)






