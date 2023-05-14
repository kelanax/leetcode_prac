'''

PROBLEM: 

Given the root of a binary tree, flatten the tree into a linked list using the same Tree class. The left 
child of the linked list is always NULL, and the right child points to the next node in the list. The 
nodes in the linked list should be in the same order as the preorder traversal of the given binary tree.

-----------------------
PATTERN: DFS
-----------------------

'''






def flatten_tree(root):

  if not root : return None
  
  current = last = root
  # prev = None

  while current : 
    if current.left :
      last = current.left
      while last.right :
        last = last.right
      
      last.right = current.right
      current.right = current.left
      current.left = None
    current = current.right


  return root








