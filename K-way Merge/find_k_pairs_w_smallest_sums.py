'''

PROBLEM: 

Given two lists, and an integer k , find k pairs of numbers with the smallest sum so that in each pair, 
each list contributes one number to the pair. 

Constraints: 
- Input lists should be sorted in ascending order. 
- If the value of k exceeds the total number of valid pairs that may be formed, return all the pairs.

----------------------
PATTERN: K-WAY MERGE
----------------------

'''



from heapq import *


def k_smallest_pairs(list1, list2, k):
    
    result = []

    p1 = p2 = next_sum = 0
    num_pairs = k
    min_heap = next_pair = []

    for _ in range(k) :
        if p1 < len(list1) and p2 < len(list2) :
            heappush(min_heap, [list1[p1] + list2[p2], list1[p1], list2[p2]])
            p2 += 1
        elif p2 >= len(list2) :
            p1 += 1
            p2 = 0
        elif p1 >= len(list1) :
            result = [[y,z] for x,y,z in min_heap]
            return result


    while num_pairs > 0 and p1 < len(list1) :

        if p1 < len(list1) and p2 < len(list2) :
            next_sum = list1[p1] + list2[p2]
        else : next_sum = float('inf')

        if min_heap and (min_heap[0][0] <= next_sum) :
            result.append([[y,z] for x,y,z in [heappop(min_heap)]][0])
        else : 
            result.append([list1[p1], list2[p2]])
            p1 = (p1 + 1) if p2 + 1 >= len(list2) else p1
            p2 = 0 if p2 + 1 >= len(list2) else p2 + 1
        
        num_pairs -= 1




    return result







