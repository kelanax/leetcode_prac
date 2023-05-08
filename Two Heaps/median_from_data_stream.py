'''

PROBLEM: 

Implement a data structure that'll store a dynamically growing list of integers and 
provide access to their median in O(1).

--------------------
PATTERN: TWO HEAPS
--------------------

'''


import heapq
# from min_heap import *
# from max_heap import *

# Tip: You may use some of the code templates provided
# in the support files

# LEFT - max heap
# RIGHT - min heap

class MedianOfStream:
  
  def __init__(self) :
    self.__max_heap = []
    heapq.heapify(self.__max_heap)

    self.__min_heap = []
    heapq.heapify(self.__min_heap)


  # This function should take a number and store it
  def insert_num(self, num):
    
    if self.__max_heap and num <= self.__max_heap[0] : 
      heapq.heappush(self.__max_heap, -num)
    elif self.__min_heap and num >= self.__min_heap[0] : 
      heapq.heappush(self.__min_heap, num)
    else : heapq.heappush(self.__max_heap, -num)


    self.__rebalance()

    
  # This function should return the median of the stored numbers
  def find_median(self):
    self.__rebalance()

    if len(self.__max_heap) == len(self.__min_heap) : 
      return float((-self.__max_heap[0] + self.__min_heap[0]) / 2)
    else : return float(-self.__max_heap[0])
  
  def __rebalance(self) :

    if len(self.__max_heap) == len(self.__min_heap) : return
    limit = (len(self.__max_heap) + len(self.__min_heap)) % 2

    if len(self.__max_heap) - len(self.__min_heap) > limit :

      while len(self.__max_heap) - len(self.__min_heap) > limit :
        val = -heapq.heappop(self.__max_heap) 
        heapq.heappush(self.__min_heap, val)

    elif len(self.__min_heap) - len(self.__max_heap) > 0 :
      while len(self.__min_heap) - len(self.__max_heap) > 0 :
        val = heapq.heappop(self.__min_heap) 
        heapq.heappush(self.__max_heap, -val)















