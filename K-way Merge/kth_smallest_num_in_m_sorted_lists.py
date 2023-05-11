'''

PROBLEM: 

Given m number of sorted lists in ascending order and an integer k , find the kth smallest 
number among all the given lists.

Constraints:
- If k is greater than the total number of elements in the input lists, return the greatest 
  element from all the lists.
- If there are no elements in the input lists, return 0.

----------------------
PATTERN: K-WAY MERGE
----------------------

'''




from heapq import *


def k_smallest_number(lists, k):

    total = len(lists) * len(lists[0])

    if total == 0 : return 0
    if k > total :
        last = [li[-1] for li in lists]
        return max(last)

    min_heap = [[li[0], i] for i, li in enumerate(lists)]
    heapify(min_heap)

    ptrs = [0] * len(lists)
    
    count = k
    kth = -1

    while count > 0 :
        if min_heap:
            kth, index = heappop(min_heap)

            if ptrs[index] < len(lists[index]) - 1 : 
                ptrs[index] += 1

                heappush(min_heap, [lists[index][ptrs[index]], index])
                count -= 1


    return kth





