"""Calculate the equation inside the list in order of operation.

The first and last item will always be a number. Numbers are
separated by a + or * symbol. All items are in individual strings.

Examples:
    
    >>> calculate(["6", "+", "8", "*", "12", "+", "47"])
    149

    >>> calculate(["1", "+", "1", "+", "1"])
    3

    >>> calculate(["1", "+", "1", "*", "1", "+", "20"])
    22

"""

def calculate(lst):
    """Mathematically calculates items inside list in order of operation."""

    new_lst = []

    if "*" in lst:
        for index in range(len(lst) - 1):
            if lst[index] == "*":
                product = int(lst[(index - 1)]) * int(lst[(index + 1)])
                new_lst.append(product)
                lst.pop(index - 1)
                new_lst.pop(index - 1)
            else:
                new_lst.append(lst[index])
        # print new_lst
    else:
        for index in range(len(lst)):
            new_lst.append(lst[index])
        # print new_lst


    another_lst = []
        
    for item in new_lst:
        if item != "+":
            another_lst.append(int(item))


    result = 0
    
    for n in another_lst:
        result += n

    return result


   
    # BRAINSTORMING IDEAS

    # if I could use sum()
    # return sum(another_lst)

    # for item in new_lst:
    #     if item % 2 != 

    # answer = 0
    # for index in range(len(new_lst) - 1):
    #     if index % 2 != 0:
    #         result = new_lst[index] + new_lst[index + 2]
    #         answer += result
    # print answer


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. AWESOMESAUCE!\n"
