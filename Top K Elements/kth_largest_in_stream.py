'''

PROBLEM: 

Given an infinite stream of integers, nums, design a class to find the kth largest element 
in a stream.

Note: It is the k th largest element in the sorted order, not the kth distinct element.

The class should have the following functions, inputs, and return values: 
- Init(): It takes an array of integers and an integer k and initializes the class object. 
- Add(value): It takes one integer value, appends it to the stream, and calls the Return kth 
  largest() function. 
- Return kth largest(): It returns an integer value that represents the kth largest element 
  in the stream.

------------------------
PATTERN: TOP K ELEMENTS
------------------------

'''


import heapq

class KthLargest:
    # constructor to initialize heap and add values in it
    def __init__(self, k, nums):
        self.min_heap = nums
        self.k = k

        heapq.heapify(self.min_heap)

        while len(self.min_heap) > self.k :
            heapq.heappop(self.min_heap)
        

    # adds element in the heap
    def add(self, val):
        heapq.heappush(self.min_heap, val)

        if len(self.min_heap) > self.k :
            heapq.heappop(self.min_heap)

        return self.return_Kth_largest()
        
    # returns kth largest element from heap
    def return_Kth_largest(self):
        
        return self.min_heap[0]

    

