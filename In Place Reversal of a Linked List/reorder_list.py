'''

PROBLEM: 

Given the head of a singly linked list, reorder the list as if it were folded on itself. 
For example, if the list is represented as follows:  
L 0 ​→  L 1 → L 2 ​→ … → 2 L n-2 ​→ L n-1 ​→  L n 
This is how you'll reorder it: 
L 0 ​→  L n →  L 1 ​→ L n-1 ​→ L 2 ​→  L n-2 ​→ … 

You don't need to modify the values in the list's nodes; only the links between nodes 
need to be changed.

--------------------------------------------
PATTERN: IN PLACE REVERSAL OF A LINKED LIST 
--------------------------------------------

'''



# from linked_list import LinkedList
# from linked_list_node import LinkedListNode
            
def reorder_list(head):

    length = get_len(head)
    if length <= 2 : return head

    starting_node = length // 2
    if length % 2 != 0 : starting_node += 2
    else : starting_node += 1

    i = 1
    prev, curr, next_node = None, head, None

    while curr and i != starting_node :
        prev = curr
        curr = curr.next
        i += 1
    
    prev.next = None
    reversed_list = reverse_nodes(curr)
    forward_list = head
    
    result = merge_lists(forward_list, reversed_list)


    
    return result

def merge_lists(list1, list2) :
    
    ptr1, ptr2 = list1, list2

    while ptr1 and ptr2 :
        temp = ptr2.next
        ptr1 = insert_after(ptr1, ptr2)
        ptr2 = temp
    
    return list1




def insert_after(prev, insert) :

    if prev :
        next_node = prev.next
        prev.next = insert
        insert.next = next_node
    return next_node
    




def reverse_nodes(head) :

    prev , curr, next_node = None, head, None

    while curr :
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    
    return prev


def get_len(head) :

    count = 0
    while head :
        head = head.next
        count += 1
    
    return count





