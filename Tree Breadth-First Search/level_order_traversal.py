'''

PROBLEM: 

Given the root of a binary tree, display the values of its nodes while performing a level order traversal. 
Return the node values for all levels in a string separated by the character ":". 

If the tree is empty, i.e., the number of nodes is 0, then return “None” as the output.

-----------------------
PATTERN: BFS
-----------------------

'''



# Import required functions
from collections import deque
# from binary_tree import *


# Tip: You may use some of the code templates provided
# in the support files

def level_order_traversal(root):

    if not root : return ""

    results = []
    q_curr = deque()
    q_next = deque()

    q_curr.append(root)

    node = root

    level = 0

    while q_curr :
        node = q_curr.popleft()
        results.append(str(node.data))

        if node.left : q_next.append(node.left)
        if node.right : q_next.append(node.right)

        if not q_curr : 
            level += 1
            q_curr, q_next = q_next, deque()


   
    return " : ".join(results)















