'''

PROBLEM: 

Find the k th smallest element in an (nxn) matrix, where each row and column of the matrix is sorted in ascending order. 
Although there can be repeating values in the matrix, each element is considered unique and, therefore, contributes to 
calculating the k th smallest element.

----------------------
PATTERN: K-WAY MERGE
----------------------

'''


from heapq import *

def kth_smallest_element(matrix, k):
    
    min_heap = []
    n = len(matrix)
    count = 0

    for i in range(0, n) :
        heappush(min_heap, (matrix[i][0], i, 0))
    
    val = 0
    while count < k :
        val, i, j = heappop(min_heap)

        if j + 1 < n :
            heappush(min_heap, (matrix[i][j+1], i, j + 1))
        count += 1


    return val



