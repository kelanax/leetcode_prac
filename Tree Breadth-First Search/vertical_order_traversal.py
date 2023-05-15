'''

PROBLEM: 

Find the vertical order traversal of a binary tree when the root of the binary tree is given. 
In other words, return the values of the nodes from top to bottom in each column, column by 
column from left to right. If there is more than one node in the same column and row, 
return the values from left to right.

-----------------------
PATTERN: BFS
-----------------------

'''





# from binary_tree import *
# from binary_tree_node import *
from collections import defaultdict, deque

# Tip: You may use some of the code templates provided
# in the support files

def vertical_order(root):
    
    hash_map = {}
    q = deque()
    min_col = max_col = 0
    solution = []

    q.append([root, 0])

    while q :
        node, col = q.popleft()
        if col in hash_map :
            hash_map[col].append(node.data)
        else : hash_map[col] = [node.data]

        if node.left : 
            q.append([node.left, col - 1])
            if col - 1 < min_col : min_col = col - 1
        if node.right : 
            q.append([node.right, col + 1])
            if col + 1 > max_col : max_col = col + 1 

    
    for i in range(min_col, max_col + 1) : 
        nodes = hash_map[i]
        solution.append(nodes)


    return solution














