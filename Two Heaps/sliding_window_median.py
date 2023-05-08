'''

PROBLEM: 

Given an integer array, nums, and an integer, k, there is a sliding window of size k, 
which is moving from the very left to the very right of the array. We can only see 
the k numbers in the window. Each time the sliding window moves right by one position. 

Given this scenario, return the median of the each window. Answers within 10^-5 
of the actual value will be accepted.

--------------------
PATTERN: TWO HEAPS
--------------------

'''






# from min_heap import *
# from max_heap import *
import heapq

# Tip: You may use some of the code templates provided
# in the support files

def median_sliding_window(nums, k):
    
    # LEFT --> MAX HEAP
    # RIGHT --> MIN HEAP

    if k == 1 : return [float(x) for x in nums]

    max_heap = []
    min_heap = []
    output = []

    window_start = 0
    window_end = window_start + k - 1

    for i in range(k) :
        if not max_heap or nums[i] <= -max_heap[0] :
            heapq.heappush(max_heap, -nums[i])
        else : heapq.heappush(min_heap, nums[i])
        
        rebalance(max_heap, min_heap)
    
    while window_start <= len(nums) - k and window_end < len(nums) : 
        median = get_median(max_heap, min_heap)
        output.append(median)
        remove_from_heap(max_heap, min_heap, nums[window_start])

        window_start += 1
        window_end = window_start + k - 1
        if window_end < len(nums) :
            if not max_heap or nums[window_end] <= -max_heap[0] :
                heapq.heappush(max_heap, -nums[window_end])
            else : heapq.heappush(min_heap, nums[window_end])
            
        rebalance(max_heap, min_heap)

    return output


def remove_from_heap(max_heap, min_heap, val) :
    if max_heap and val == -max_heap[0] : heapq.heappop(max_heap)
    elif min_heap and val == min_heap[0] : heapq.heappop(min_heap)
    else :
        if max_heap and val <= -max_heap[0] and -val in max_heap :
            index = max_heap.index(-val)
            max_heap[index] = max_heap[-1]
            max_heap.pop()
            heapq.heapify(max_heap)
        elif min_heap and val >= min_heap[0] and val in min_heap :
            index = min_heap.index(val)
            min_heap[index] = min_heap[-1]
            min_heap.pop()
            heapq.heapify(min_heap)
        
    rebalance(max_heap, min_heap)


def get_median(max_heap, min_heap) :
    if len(max_heap) == len(min_heap) :
        return float( ( -max_heap[0] + min_heap[0] ) / 2)
    else : return float(-max_heap[0])


def rebalance(max_heap, min_heap) :
    if max_heap and len(max_heap) > len(min_heap) + 1 :
        val = -heapq.heappop(max_heap)
        heapq.heappush(min_heap, val)
    elif min_heap and len(min_heap) > len(max_heap) :
        val = heapq.heappop(min_heap)
        heapq.heappush(max_heap, -val)


   































#  WRONG CODE---------------------------------

'''
from min_heap import *
from max_heap import *
import heapq

# Tip: You may use some of the code templates provided
# in the support files

def median_sliding_window(nums, k):
    
    # LEFT --> MAX HEAP
    # RIGHT --> MIN HEAP

    max_heap = []
    min_heap = []
    output = []

    window_start = 0
    window_end = window_start + k - 1

    if k % 2 == 1 :

        while window_start <= len(nums) - k and window_end < len(nums) :
            index = int((window_start + window_end) / 2)
            print('index:', index)
            median = float( nums[index] )
            output.append(median)
            window_start += 1
            window_end = window_start + k - 1
    else :
        for i in range(k) :
            if not max_heap or nums[i] <= -max_heap[0] :
                heapq.heappush(max_heap, nums[i])
            else : heapq.heappush(min_heap, nums[i])
            
            rebalance(max_heap, min_heap)
        
        while window_start <= len(nums) - k and window_end < len(nums) : 
            median = get_median(max_heap, min_heap)
            output.append(median)
            remove_from_heap(max_heap, min_heap, nums[window_start])

            window_start += 1
            window_end = window_start + k - 1
            if window_end < len(nums) :
                if not max_heap or nums[window_end] <= -max_heap[0] :
                    heapq.heappush(max_heap, nums[window_end])
                else : heapq.heappush(min_heap, nums[window_end])
                
            rebalance(max_heap, min_heap)

    return output


def remove_from_heap(max_heap, min_heap, val) :
    if max_heap and val == -max_heap[0] : heapq.heappop(max_heap)
    elif min_heap and val == min_heap[0] : heapq.heappop(min_heap)
    else :
        if max_heap and val <= max_heap[0] and val in max_heap :
            index = max_heap.index(val)
            max_heap[index] = max_heap[-1]
            max_heap.pop()
            heapq.heapify(max_heap)
        elif min_heap and val >= min_heap[0] and val in min_heap :
            index = min_heap.index(val)
            min_heap[index] = min_heap[-1]
            min_heap.pop()
            heapq.heapify(min_heap)
        
        rebalance(max_heap, min_heap)


def get_median(max_heap, min_heap) :
    if len(max_heap) == len(min_heap) :
        return float( ( -max_heap[0] + min_heap[0] ) / 2)
    else : return -max_heap[0]


def rebalance(max_heap, min_heap) :
    if max_heap and len(max_heap) > len(min_heap) + 1 :
        val = -heapq.heappop(max_heap)
        heapq.heappush(min_heap, val)
    elif min_heap and len(min_heap) < len(max_heap) :
        val = heapq.heappop(min_heap)
        heapq.heappush(max_heap, -val)




'''

