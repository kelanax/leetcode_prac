'''

PROBLEM: 

Given a string, rearrange it so that any two adjacent characters are not the same. 
If such a reorganization of the characters is possible, output any possible valid 
arrangement. Otherwise, return an empty string.

------------------------
PATTERN: TOP K ELEMENTS
------------------------

'''

# importing libraries
from collections import Counter
import heapq

def reorganize_string(input_string):
    
    output = [""] * len(input_string) 
    counter = Counter(input_string)

    max_heap = [[-val, key] for key, val in counter.items()]
    heapq.heapify(max_heap)

    if len(input_string) % 2 == 0 and (-max_heap[0][0]) > len(input_string) // 2 :
        return ""
    elif (-max_heap[0][0]) > (len(input_string) // 2) + 1 : 
        return ""

    
    i = 0
    previous = None
    while i < len(input_string) : 

        if max_heap :
            
            freq, char = heapq.heappop(max_heap)

            output[i] = char

            i += 1
            freq += 1

            if previous :
                heapq.heappush(max_heap, previous)
                previous = None

            if i < len(input_string) and freq < 0 : 
                previous = [freq,char]
        
        elif previous : return ""
        else : break
        



    return ''.join(output)






