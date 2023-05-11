'''

PROBLEM: 



------------------------
PATTERN: TOP K ELEMENTS
------------------------

'''


import heapq

def top_k_frequent(arr, k):

    freq_dict = {}

    for i in range(len(arr)) :
        if arr[i] in freq_dict : freq_dict[arr[i]] = freq_dict[arr[i]] + 1
        else : freq_dict[arr[i]] = 1
    
    min_heap = [[val, key] for key,val in freq_dict.items()]
    heapq.heapify(min_heap)

    while len(min_heap) > k :
        heapq.heappop(min_heap)
    return [key for val, key in min_heap]
    


