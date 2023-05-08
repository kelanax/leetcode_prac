'''

PROBLEM: 

Given a singly linked list, swap every two adjacent nodes of the linked list. 
After the swap, return the head of the linked list.

Note: Solve the problem without modifying the values in the list’s nodes. 
In other words, only the nodes themselves can be changed.

--------------------------------------------
PATTERN: IN PLACE REVERSAL OF A LINKED LIST 
--------------------------------------------

'''



# from linked_list_node import *
# from linked_list import *


def swap_pairs(head):
    
    if not head.next : return head
    curr, prev = head, None
    # prev, curr, next_node = None, head, head.next
    head = head.next

    while curr and curr.next :
        
        remainder = curr.next.next

        right = curr.next
        right.next = curr
        curr.next = remainder 

        if not prev : prev = curr
        else : 
            prev.next = right
            prev = curr

        curr = remainder

    

    return head




