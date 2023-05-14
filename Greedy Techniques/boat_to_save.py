'''

PROBLEM: 

You're given an array, people, where people[i] is the weight of the  th person, and an infinite 
number of boats, where each boat can carry a maximum weight, limit. Each boat carries, at most, 
two people at the same time. This is provided that the sum of the weight of those people is 
nder or equal to the weight limit. You need to return the minimum number of boats to carry 
every person in the array.

---------------------------
PATTERN: GREEDY TECHNIQUES
---------------------------

'''



def rescue_boats(people, limit):
    
    people.sort()
    light = 0
    heavy = len(people) - 1
    boats = 0  

    while light <= heavy :
        if light == heavy : 
            boats += 1
            break
        
        if people[light] + people[heavy] <= limit :
            boats += 1
            light += 1
            heavy -= 1
        else :
            heavy -= 1
            boats += 1


    return boats





