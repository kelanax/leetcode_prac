'''
PROBLEM: 

In a single-player jump game, the player starts at one end of a series of squares, 
with the goal of reaching the last square. 

At each turn, the player can take up to s steps towards the last square, where s is 
the value of the current square. 

For example, if the value of the current square is 3 , the player can take either 3 steps, 
or 2 steps, or 1 1 step in the direction of the last square. The player cannot move in the 
opposite direction, that is, away from the last square. 

You have been tasked with writing a function to validate whether a player can win a given 
game or not. You've been provided with the nums integer array, representing the series of 
squares. The player starts at the first index and, following the rules of the game, tries 
to reach the last index. 

If the player can reach the last index, your function returns TRUE; otherwise, it returns 
FALSE.

---------------------------
PATTERN: GREEDY TECHNIQUES
---------------------------

'''



def gas_station_journey(gas, cost):
    if sum(cost) > sum(gas) : return -1
    n = len(gas)

    for i in range(n) :

        start = i
        curr_gas = 0

        while True : 
            curr_gas = curr_gas + gas[start] - cost[start]
            # print("i:", i, ", start:", start, "curr_gas:", curr_gas)

            if curr_gas >= 0 :
                start += 1
                start = start % n
                if curr_gas == 0 and start != i : break
            elif curr_gas < 0 : break

            if start == i : return i

    return -1


