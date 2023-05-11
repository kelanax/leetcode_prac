'''

PROBLEM: 

Given an array of k sorted linked lists, your task is to merge them into a single sorted list.

----------------------
PATTERN: K-WAY MERGE
----------------------

'''


from linked_list import LinkedList
from linked_list_node import LinkedListNode

# Tip: You may use some of the code templates provided
# in the support files

def merge_k_lists(lists):
    
    i = 0
    j = len(lists) - 1
    

    return merge_helper(lists, i , j)


    
def merge_helper(lists, i , j) :

    if i == j :
        return lists[i].head
    
    if j - i == 1 :
        return merge_step(lists[i].head, lists[j].head)
    
    output1 = merge_helper(lists, i, ((i+j) // 2))
    output2 = merge_helper(lists, ((i+j) // 2) + 1, j)

    return merge_step(output1, output2)


def merge_step(p1, p2) :

    head = prev = None
    
    while p1 and p2 :
        if p1.data <= p2.data : 
            if head and prev :
                prev.next, prev = p1, p1
                p1 = p1.next
            else : 
                head, prev = p1, p1
                p1 = p1.next
        else :
            if head and prev :
                prev.next, prev = p2, p2
                p2 = p2.next
            else : 
                head, prev = p2, p2
                p2 = p2.next

    while p1 :
        prev.next, prev = p1, p1
        p1 = p1.next
    
    while p2 :
        prev.next, prev = p2, p2
        p2 = p2.next
    
    return head





