'''

PROBLEM: 

Given the root of a binary tree, return the maximum sum of any non-empty path.

A path in a binary tree is defined as follows:

- A sequence of nodes in which each pair of adjacent nodes must have an edge connecting them.
    - A node can only be included in a path once at most.
    - Including the root in the path is not compulsory.

You can calculate the path sum by adding up all node values in the path. To solve this problem, 
calculate the maximum path sum given the root of a binary tree so that there won’t be any greater 
path than it in the tree.

-----------------------
PATTERN: DFS
-----------------------

'''





# from binary_tree import *
# from binary_tree_node import *


class MaxTreePathSum:
    def __init__(self):
        self.max_sum = float('-inf')


    def max_path_sum(self, root):   
        
        if not root : return 0

        left, left_combo = self.helper(root.left)
        right, right_combo = self.helper(root.right)
        curr = root.data
        curr_combo = left + curr + right

        self.max_sum = max(self.max_sum, left + curr, right + curr, curr, curr_combo, left_combo, right_combo)
        

        return self.max_sum

    def helper(self, root) :
        if not root : return 0,0
        elif not root.left and not root.right : return root.data, root.data

        left, left_combo = self.helper(root.left)
        right, right_combo = self.helper(root.right)
        
        curr = root.data
        curr_combo = left + curr + right

        self.max_sum = max(self.max_sum, left + curr, right + curr, curr, left_combo, right_combo, curr_combo)

        return max(left + curr, right + curr, curr) , left + curr + right











