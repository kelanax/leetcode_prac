'''

PROBLEM: 

Given a binary tree, connect all nodes of the same hierarchical level. We need to connect them 
from left to right, so that the next pointer of each node points to the node on its immediate 
right. The next pointer of the right-most node at each level will be NULL. 

For this problem, each node in the binary tree has one additional pointer (the next pointer) 
along with the left and right pointers.

-----------------------
PATTERN: BFS
-----------------------

'''


# THIS USES MORE SPACE THAN NECESSARY --> ONCE YOU HAVE A LEVEL, YOU CAN TRAVERSE IT AND CONNCECT IT'S CHILDREN WITH NO EXTRA SPACE NEEDED


from binary_tree import *
from binary_tree_node import *
from collections import deque

# Function to populate same level pointers
def populate_next_pointers(node):

    # if not node : return
    # if not node.left and not node.right : return

    q = deque()
    q.append(node)

    prev = curr = None

    while q :

        n = len(q)

        for _ in range(n) :
            curr = q.popleft()
            if prev :
                prev.next = curr
                prev = curr
            else :
                prev = curr
            
            if curr.left : q.append(curr.left)
            if curr.right : q.append(curr.right)
        
        prev.next = None
        prev = curr = None






'''

# Helper function to connect all children nodes at the next level
def connect_next_level(head):
    #   Declaring the necessary pointers
    current = head
    next_level_head = None
    prev = None

    while current:
        if current.left and current.right:
            # If both current node children are not null
            # then connect them with each other and previous
            # nodes in the same level.
            if not next_level_head:
                next_level_head = current.left

            current.left.next = current.right

            if prev:
                prev.next = current.left

            prev = current.right
        elif current.left:
            # If only the left child node is not null
            # then only connect it with previous same level nodes
            if not next_level_head:
                next_level_head = current.left

            if prev:
                prev.next = current.left

            prev = current.left
        elif current.right:
            # If only the right child node children is not null
            # then only connect it with previous same level nodes
            if not next_level_head:
                next_level_head = current.right

            if prev:
                prev.next = current.right

            prev = current.right

        # Update current pointer
        current = current.next

    # Pointing the last node (right-most node) of the next level
    # to None
    if prev:
        prev.next = None

    # Return the head node (left-most node) of the next level
    return next_level_head


# Function to populate same level pointers
def populate_next_pointers(node):
    if node:
        node.next = None

        while True:
            node = connect_next_level(node)
            if not node:
                break



'''

















# Do not modify the code below
# Function to find the given node and return its next node
def get_next_node(node, node_data):
    # Performing Binary Search
    while node and node_data != node.data:
        if node_data < node.data:
            node = node.left
        else:
            node = node.right

    # If node is not found return -1 else return its next node
    if not node:
        non_existing_node = BinaryTreeNode(-1)
        return non_existing_node
    else:
        return node.next
















