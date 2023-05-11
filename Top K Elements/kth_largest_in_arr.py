'''

PROBLEM: 

Find the kth largest element in an unsorted array. Note: We need to find the kth largest 
element in the sorted order, not the kth distinct element.

------------------------
PATTERN: TOP K ELEMENTS
------------------------

'''

import heapq

def find_kth_largest(arr, k):

    min_heap = []

    for i in range(k) :
        heapq.heappush(min_heap, arr[i])
    
    for i in range(k, len(arr)) :
        if arr[i] > min_heap[0] :
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, arr[i])

    
    return heapq.heappop(min_heap)


