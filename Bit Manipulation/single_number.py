'''

PROBLEM: 

Given an array of integers in which every element in the list appears twice 
except for one, find the element that occurs once.

---------------------------
PATTERN: BIT MANIPULATION
---------------------------

'''




def single_number(nums):
    result = 0

    for val in nums :
        result = result ^ val

    return result






