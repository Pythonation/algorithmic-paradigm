def greedy_coins(Value):
    coins = [1, 2, 5, 10, 20, 50,100, 500 ] 
    n = len(coins) - 1
    result = []
    
    while n >= 0 :
        while Value >= coins[n]:    
            Value -= coins[n]
            result.append(coins[n])
        n -= 1
    return (result)


print( greedy_coins(1654) )


