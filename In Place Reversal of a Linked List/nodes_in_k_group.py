'''

PROBLEM: 

Given a linked list, reverse the nodes of the linked list k at a time and return the 
modified list. Here, k is a positive integer and is less than or equal to the length 
of the linked list. If the number of nodes is not a multiple of k, the nodes left in 
the end will remain in their original order.

You can’t alter the values of the linked list nodes. Only the nodes themselves may 
be changed.

--------------------------------------------
PATTERN: IN PLACE REVERSAL OF A LINKED LIST 
--------------------------------------------

'''


import math
# from linked_list import LinkedList
# from linked_list_node import LinkedListNode
# from linked_list_traversal import traverse_linked_list
# from linked_list_reversal import reverse_linked_list
            
def reverse_linked_list(head, k):
  
    count = count_linked_list(head)

    if count < k : return head

    new_list = prev = None
    curr = head
    new_list_tail = curr_last = None
    first_append = found_list_head = False

    while curr and count >= k :
        prev = None
        for _ in range(k) :
            if curr :
                next_node = curr.next
                curr.next = prev
                prev = curr

                curr = next_node
                count -= 1

                if not first_append : 
                    curr_last = prev
                    first_append = True

        first_append = False
        if not found_list_head : 
            new_list = prev
            found_list_head = True
                
        if new_list_tail :
            new_list_tail.next = prev
            new_list_tail = curr_last
        else: 
            new_list_tail = curr_last
        
    
    if new_list_tail :
            new_list_tail.next = prev
            new_list_tail = curr_last
    if curr_last : curr_last.next = curr

    return new_list





def count_linked_list(head) :
    count = 0

    while head :
        count += 1
        head = head.next
    
    return count





