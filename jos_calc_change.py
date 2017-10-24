def calc_change(n):
    
    penny = 1
    nickle = 5
    dime = 10
    quarter = 25
    
    coins = {
        quarter: 0,
        dime: 0,
        nickle: 0,
        penny: 0
    }
    
    
    while n > 0:
        if n >= quarter:
            n -= 25
            coins[quarter] += 1
        elif n >= dime:
            n -= 10
            coins[dime] += 1
        elif n >= nickle:
            n -= 5
            coins[nickle] += 1
        else:
            n -= penny
            coins[penny] += 1
    
    print coins
    
calc_change(55)
