'''

PROBLEM: 

A thief has discovered a new neighborhood to target, where the houses can be represented as 
nodes in a binary tree. The money in the house is the data of the respective node. The thief 
can enter the neighborhood from a house represented as root of the binary tree. Each house has 
only one parent house. The thief knows that if he robs two houses that are directly connected, 
the police will be notified. The thief wants to know the maximum amount of money he can steal 
from the houses without getting caught by the police. The thief needs your help determining the 
maximum amount of money he can rob without alerting the police.

-----------------------
PATTERN: BACKTRACKING
-----------------------

'''




from binary_tree import *
from collections import deque

def rob(root):
  
  result = max(helper(root, False), helper(root, True))

  return result



def helper(root, isParentRobbed) :

  if not root : return 0
  if (not root.left) and (not root.right) :
    if isParentRobbed : return 0
    else : return root.data

  max_sum = 0
  if isParentRobbed :
    max_sum += helper(root.left, False)
    max_sum += helper(root.right, False)
    return max_sum
  else :
    max_sum += helper(root.left, False)
    max_sum += helper(root.right, False)

    ret_val = root.data
    ret_val += helper(root.left, True)
    ret_val += helper(root.right, True)
    max_sum = max(max_sum, ret_val)

    return max_sum

















