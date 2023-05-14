'''

PROBLEM: 

Given a binary tree, you need to compute the length of the tree’s diameter. The diameter of a binary tree 
is the length of the longest path between any two nodes in a tree. This path may or may not pass through 
the root. 


Note: The length of the path between two nodes is represented by the number of edges between them.

-----------------------
PATTERN: DFS
-----------------------

'''







from binary_tree_node import *
from binary_tree import *


def diameter_of_binaryTree(root):
  
  res = helper(root)
  max_val = max(res[0], res[1])

  return max_val




def helper(root) :
  if not root : return [0,0]
  if (not root.left) and (not root.right) : return [0,0]
  
  left = 1 + (helper(root.left))[0] if root.left else 0
  right = 1 + (helper(root.right))[0] if root.right else 0

  max_val = max(left, right)

  return [max_val, left + right]














