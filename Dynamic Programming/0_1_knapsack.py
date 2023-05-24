'''

Suppose you have the list of weights and corresponding values for n items. You have 
a knapsack that can carry a specific amount of weight at a time called capacity.

You need to find the maximum profit of items using the sum of values of the items 
you can carry in a knapsack. The sum of the weights of the items should be less than 
or equal to the knapsack's capacity.

If any combination can't make the given knapsack capacity of weights, then return 0.

------------------------------
PATTERN: DYNAMIC PROGRAMMING
------------------------------

'''





def find_max_knapsack_profit(capacity, weights, values):

    n = len(weights)
    # dp = [[0] * (n + 1) for _ in range(n)]
    dp = [[0] * (capacity + 1) for _ in range(n)]

    def print_dp(dp) :
        print('DP Table: ')
        for i in range(len(dp)) :
            print('\t', dp[i])


    for row in range(n) :
        print_dp(dp) 

        for col in range(0, capacity + 1) :
            # col_ = col - 1
            # print("row:", row, "col:", col)
            if row == 0 and col == 0 : continue

            if row == 0 :
                # print("row:", row, "col:", col)
                if weights[row] > capacity or weights[row] > col : 
                    # print('dp:\n', dp)
                    continue
                else : 
                    dp[row][col] = values[row]
                    # print('dp:\n', dp)
            else :
                
                if col == 0 : continue

                weight = weights[row]
                value = values[row]
                prev_val_if_choosen = 0
                

                if weight > capacity  or weight > col: 
                    dp[row][col] = dp[row - 1][col]
                    # print('entered 0')
                    # print('dp:\n', dp)
                    continue

                if (col - weight >= 0) : prev_val_if_choosen = dp[row - 1][col - weight]
                dp[row][col] = max(dp[row - 1][col], prev_val_if_choosen + value)
                # print('entered 1')
                # print('dp:\n', dp)


    result = dp[n-1][capacity]

    print_dp(dp) 
    
    return result  





'''

def find_max_knapsack_profit(capacity, weights, values):
    values_length = len(values)
    if capacity <= 0 or values_length == 0 or len(weights) != values_length:
        return 0
    
    profits = [0] * (capacity + 1)

    for i in range(values_length):
        for c in range(capacity, -1, -1):
            if weights[i] <= c:
                new_profit = profits[c - weights[i]] + values[i]
                profits[c] = max(profits[c], new_profit)
    return profits[capacity]


'''









