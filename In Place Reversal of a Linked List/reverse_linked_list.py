'''

PROBLEM: 
Given the head of a singly linked list, reverse the linked list and return its updated head.


--------------------------------------------
PATTERN: IN PLACE REVERSAL OF A LINKED LIST 
--------------------------------------------

'''


# from linked_list import LinkedList
# from linked_list_node import LinkedListNode
            
def reverse(head):

    prev = None
    curr = head

    while curr : 
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    
    return prev



