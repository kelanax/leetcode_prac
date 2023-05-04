'''
PROBLEM: 

For the given head of the linked list, find out if the linked list is a palindrome or not. 
Return TRUE if the linked list is a palindrome. Otherwise, return FALSE.

--------------------------------
PATTERN: FAST AND SLOW POINTER  
--------------------------------
*didn't use here though --> could've used to reverse the linked list

'''




from linked_list import LinkedList
from linked_list_reverse import reverse_linked_list
from print_list import print_list_with_forward_arrow


def palindrome(head):

   size = get_linked_list_len(head)
   
   res_node, res_bool = palindrome_helper(head, size)
   return res_bool
    

def palindrome_helper(head, size) :

    if size == 0 : return head, True
    if size == 1 : return head.next, True

    res_node, res_bool = palindrome_helper(head.next, size - 2)

    if not res_bool : return None, False
    elif res_node.data == head.data :
        return res_node.next, True 

    return None, False

def get_linked_list_len(head) :
    size = 0

    while head is not None : 
        size += 1
        head = head.next

    return size


def rev_list(node) :
    new_list = None

    while node :

        tail = node.next

        node.next = new_list
        new_list = node

        node = tail
    
    return new_list

   