'''

PROBLEM: 

Given a binary tree, return its zigzag level order traversal. The zigzag level order traversal 
corresponds to traversing nodes from left to right for one level, and then right to left for 
the next level, and so on, reversing direction after every level.

-----------------------
PATTERN: BFS
-----------------------

'''




# from binary_tree import *
from collections import deque

def zigzag_level_order(root):
    
    # if not root or (not root.left and not root.right) :
    #     return root

    results = []
    q = deque()
    q.append(root)
    reverse_dir = False

    while q :
        n = len(q)
        curr_path = []
        for i in range(n) :
            if reverse_dir :
                node = q.pop()
                curr_path.append(node.data)

                if node.left : q.appendleft(node.left)
                if node.right : q.appendleft(node.right)
            else :
                node = q.popleft()
                curr_path.append(node.data)

                if node.left : q.append(node.left)
                if node.right : q.append(node.right)

        reverse_dir = not reverse_dir
        results.append(curr_path)

    return results




















