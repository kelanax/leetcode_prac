'''

PROBLEM: 

Given the root node of a binary tree, convert the binary tree into its mirror image.

-----------------------
PATTERN: DFS
-----------------------

'''





from binary_tree import *
from binary_tree_node import *

def mirror_binary_tree(root):
  
  helper(root)

  return root


def helper(root) :

  if not root : return

  helper(root.left)
  helper(root.right)

  root.left, root.right = root.right, root.left












