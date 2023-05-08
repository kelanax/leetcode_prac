'''

PROBLEM: 

Given the linked list and an integer k , return the head of the linked list after 
swapping the values of the k th node from the beginning and the k th node from the 
end of the linked list.

--------------------------------------------
PATTERN: IN PLACE REVERSAL OF A LINKED LIST 
--------------------------------------------

'''



# from linked_list import LinkedList
# from linked_list_node import LinkedListNode
# from swap_two_nodes import swap
            
def swap_nodes(head, k):

    length = get_len(head)
    if length < k : return head
    if length == 2 : 
        head, head.next = head.next, head
        head.next.next = None
        return head

    print('length:', length, ', left:', k, ', right:' , length - k)

    i = 1
    prev_left = prev_right = None
    left = right = head
    while left and i < k :
        prev_left = left
        left = left.next
        i += 1
    
    if prev_left : print('prev_left:', prev_left.data, ', left:', left.data)
    elif left : print('left:', left.data)
    i = 1
    while right and i <= length - k :
        prev_right = right
        right = right.next
        i += 1
    
    if prev_right : print('prev_right:', prev_right.data, ', right:', right.data)
    elif right : print('right:', right.data)
    swap(prev_left, left, prev_right, right)
    
    if prev_right : return head
    else : return left

    # return head
    

def swap(prev_left, left, prev_right, right) :
    
    if prev_left : prev_left.next = right
    if prev_right : prev_right.next = left

    left.next, right.next = right.next, left.next
    

def get_len(head) :

    count  = 0
    while head :
        count += 1
        head = head.next
    
    return count




