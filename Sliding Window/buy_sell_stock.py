'''

PROBLEM: 

Given an array where the element at the index i represents the price of a stock on day i, 
find the maximum profit that you can gain by buying the stock once and then selling it.

Note: Stock can only be purchased on a single day and sold on a different day. 
If no profit can be achieved, we return zero.

-------------------------
PATTERN: SLIDING WINDOW  
-------------------------

'''



def max_profit(stock_prices):
    
    if len(stock_prices) <= 1 : return 0

    max_profit = 0
    buy = stock_prices[0]

    for i in range(1, len(stock_prices)) : 
        
        if stock_prices[i] < buy : buy = stock_prices[i]
        elif stock_prices[i] - buy > max_profit :
            max_profit = stock_prices[i] - buy

    return max_profit



# OLD CODE: O(N^2) -------------------------------------------------------------
def max_profit(stock_prices):
    
    if len(stock_prices) <= 1 : return 0

    max_profit = 0

    for buy in range(len(stock_prices) - 1) : 
        sell = buy + 1
        while sell < len(stock_prices) :
            if stock_prices[sell] - stock_prices[buy] > max_profit :
                max_profit = stock_prices[sell] - stock_prices[buy]
            sell += 1

    return max_profit

