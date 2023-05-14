'''

PROBLEM: 

Serialize a given binary tree to a file and deserialize it back to a tree. Make sure 
that the original and the deserialized trees are identical.

Serialize: Write the tree to a file.
Deserialize: Read from a file and reconstruct the tree in memory.

Serialize the tree into a list of integers, and then, deserialize it back from the list to a tree. 
For simplicity's sake, there's no need to write the list to the files.

-----------------------
PATTERN: DFS
-----------------------

'''


############## CODE IS STILL BUGGY #############


from binary_tree import *
from binary_tree_node import *

# Initializing our marker
MARKER = "M"
m = 1


def serialize_rec(node, stream):
    global m
    # Adding marker to stream if the node is None
    if node is None:
        stream.append(MARKER + str(m))
        m += 1
        return

    # Adding node to stream
    stream.append(node.data)

    # Doing a pre-order tree traversal for serialization
    serialize_rec(node.left, stream)
    serialize_rec(node.right, stream)

# Function to serialize tree into list of integers.


def serialize(root):
    stream = []
    serialize_rec(root, stream)
    return stream


def deserialize_helper(stream):
    # pop last element from list
    val = stream.pop()

    # Return None when a marker is encountered
    if type(val) is str and val[0] == MARKER:
        return None

    # Creating new Binary Tree Node from current value from stream
    node = BinaryTreeNode(val)

    # Doing a pre-order tree traversal for serialization
    node.left = deserialize_helper(stream)
    node.right = deserialize_helper(stream)

    # Return node if it exists
    return node

# Function to deserialize integer list into a binary tree.

def deserialize(stream):
    stream.reverse()
    node = deserialize_helper(stream)
    return node

# driver code
def main():
    global m
    input_trees = [
        [100, 50, 200, 25, 75, 350],
        [100, 200, 75, 50, 25, 350],
        [200, 350, 100, 75, 50, 200, 25],
        [100, 50, 200, 25, 75, 350],
        [25, 50, 75, 100, 200, 350],
        [350, 75, 25, 200, 50, 100]
    ]

    indx = 1
    for i in input_trees:
        tree = BinaryTree(i)
        org_tree = tree.get_tree_deep_copy()

        print(indx, ".\tBinary Tree:", sep="")
        indx += 1
        if org_tree.root is None:
            display_tree(None)
        else:
            display_tree(org_tree.root)

        print("\n\tMarker used for NULL nodes in serialization/deserialization: ",
              MARKER, "*", sep="")

        # Serialization
        ostream = serialize(tree.root)
        print("\n\tSerialized integer list:")
        print("\t" + str(ostream))

        # Deserialization
        deserialized_root = deserialize(ostream)
        print("\n\tDeserialized binary tree:")
        display_tree(deserialized_root)
        print("-"*100)
        m = 1


if __name__ == '__main__':
    main()










