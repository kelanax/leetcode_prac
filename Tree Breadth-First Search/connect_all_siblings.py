'''

PROBLEM: 

The task is to connect all nodes in a binary tree. Connect them from left to right so that the 
next pointer of each node points to the node on its immediate right. The next pointer of the 
right-most node at each level should point to the first node of the next level in the tree. 
Each node in the given binary tree for this problem includes a next pointer, along with the left 
and right pointers. Your solution must set the next pointer to connect the same level nodes to 
each other and across levels.

-----------------------
PATTERN: BFS
-----------------------

'''





# from binary_tree import *
# from binary_tree_node import *


# Tip: You may use some of the code templates provided
# in the support files

# Function to populate same level pointers
# Function to populate same level pointers
def populate_next_node_pointers(root):
    
    level_head = root
    last_tail = None

    while level_head :
        first, last = connect_next_level(level_head)

        if last_tail : 
            last_tail.next = first
            last_tail = last
        else :
            last_tail = last
        
        level_head = first



    return root


def connect_next_level(node) :

    if not node : return None, None


    current = node
    next_level_head = None
    prev = None

    while current :
        if current.left and current.right :
            left = current.left
            right = current.right

            if prev :
                prev.next = left
                prev = right
            else : prev = right

            left.next = right
            

            if not next_level_head : next_level_head = left
        elif current.left :

            left = current.left
            if not next_level_head : next_level_head = left

            if prev : 
                prev.next = left
                prev = left
            else : prev = left
        elif current.right :

            right = current.right
            if not next_level_head : next_level_head = right

            if prev : 
                prev.next = right
                prev = right
            else : prev = right

        current = current.next
        if prev : prev.next = None
        
    return next_level_head, prev







