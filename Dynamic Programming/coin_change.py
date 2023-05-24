'''

You're given an integer total and a list of integers called coins. The variable coins 
hold a list of coin denominations, and total is the total amount of money.

You have to find the minimum number of coins that can make up the total amount by 
using any combination of the coins. If the amount can't be made up, return -1. 
If the total amount is 0, return 0.

------------------------------
PATTERN: DYNAMIC PROGRAMMING
------------------------------

'''



def coin_change(coins, total):
    
    if len(coins) == 0 or total <= 0 : return 0

    dp = [[-1]*(total + 1) for _ in range(len(coins))]

    return helper(coins, dp, 0, total)




def helper(coins, dp, denom, remaining) :

    if denom >= len(coins) : 
        
        if remaining > 0 or remaining < 0: return -1
        elif remaining == 0 : return 0

    if dp[denom][remaining] > 0 : return dp[denom][remaining]


    coin = coins[denom]
    min_coins = -1

    i = 0
    amount_remaining = remaining - (i * coin)

    while amount_remaining >= 0 :

        ways = helper(coins, dp, denom + 1, amount_remaining)
        if ways < 0 and (min_coins < 0 or min_coins > 0) : 
            i += 1
            amount_remaining = remaining - (i * coin)
            continue
        else :
            if min_coins < 0 and ways >= 0 : min_coins = ways + i
            elif min_coins > 0 and ways >= 0 : min_coins = min(min_coins, i + ways)
            else : min_coins = -1

        i += 1
        amount_remaining = remaining - (i * coin)
    
    dp[denom][remaining] = min_coins

    return min_coins


    


'''

def calculate_minimum_coins(coins, rem, counter):  
    if rem < 0: 
        return -1
    if rem == 0:
        return 0
    if counter[rem - 1] != float('inf'):
        return counter[rem - 1]
    minimum = float('inf')

    for s in coins: 
        result = calculate_minimum_coins(coins, rem - s, counter)
        if result >= 0 and result < minimum:
            minimum = 1 + result

    counter[rem - 1] =  minimum if minimum !=  float('inf') else  -1 
    return counter[rem - 1]

def coin_change(coins, total): 
    if total < 1:
        return 0
    return calculate_minimum_coins(coins, total, [float('inf')] * total)

'''









