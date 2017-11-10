def fizz_buzz2(n):

    for num in range(1, n+1):

        print num

        if num % 3 == 0:
            print "fizz"

        if num % 5 == 0:
            print "buzz"

fizz_buzz2(15)
