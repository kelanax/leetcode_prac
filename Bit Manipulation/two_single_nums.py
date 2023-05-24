'''

PROBLEM: 

Given a non-empty array arr, in which exactly two elements appear once 
and all the other elements appear twice, return the two elements that 
come only once. 

Note: The result can be returned in any order. The solution should 
use constant space.

---------------------------
PATTERN: BIT MANIPULATION
---------------------------

'''





def two_single_numbers(arr):
    
    if not arr : return []

    bitwise_sum = result = 0
    output = []

    for num in arr : bitwise_sum = bitwise_sum ^ num

    n = bitwise_sum
    count = 0
    while not n & 1 :
        n = n >> 1
        count += 1
    right_bit = 1 << count

    for num in arr :
        if right_bit & num :
            result = result ^ num
    
    output.append(result)
    output.append(result ^ bitwise_sum)
    
    return output




