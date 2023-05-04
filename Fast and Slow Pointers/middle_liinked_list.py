
'''

PROBLEM:
Given a singly linked list, return the middle node of the linked list. If the number of nodes 
in the linked list is even, return the second middle node.

--------------------------------
PATTERN: FAST AND SLOW POINTER
--------------------------------

'''


# from linked_list import LinkedList

def get_middle_node(head):
    
    slow = head
    fast = head

    while fast and fast.next :

        slow = slow.next
        fast = fast.next.next
        print("fast:", fast, ", slow:", slow)

    return slow