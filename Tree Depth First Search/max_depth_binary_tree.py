'''

PROBLEM: 

Given the root of a binary tree, return its maximum depth. A binary tree's maximum depth is the number 
of nodes along the longest path from the root node down to the farthest leaf node.

-----------------------
PATTERN: DFS
-----------------------

'''




# from binary_tree import *
# from collections import deque

def max_depth(root):
    
    return helper(root)



def helper(root) :

    if not root : return 0

    left = helper(root.left)
    right = helper(root.right)

    return max(left, right) + 1












