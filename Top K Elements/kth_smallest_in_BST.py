'''

PROBLEM: 

Given the root node of a binary search tree and an integer value k, return the kth 
smallest value from all the nodes of the tree.

------------------------
PATTERN: TOP K ELEMENTS
------------------------

'''


# from binary_tree_node import *
# from binary_tree import *


def kth_smallest_element(root, k):
    
    tree = []

    search_BST(root, tree)
    print("tree:", tree)

    return tree[k-1]
        




def search_BST(root, output) :

    if root == None : return

    search_BST(root.left, output)
    output.append(root.data)
    search_BST(root.right, output)




