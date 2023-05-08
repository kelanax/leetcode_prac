'''

PROBLEM: 

You’re given the head of a singly linked list with n nodes and two positive integers, 
left and right. Our task is to reverse the list’s nodes from position left to position 
right and return the reversed list.

--------------------------------------------
PATTERN: IN PLACE REVERSAL OF A LINKED LIST 
--------------------------------------------

'''



# from linked_list import LinkedList
# from linked_list_node import LinkedListNode
# from linked_list_traversal import traverse_linked_list
# from linked_list_reversal import reverse_linked_list
            
def reverse_between(head, left, right):

  length = find_len(head)
  if length < right - left + 1 : return head

  result = head
  prev, curr = None, head
  i = 1


  while i != left :
    prev = curr
    curr = curr.next
    i += 1

  first = reverse_k_nodes(curr, right - left)

  if prev : prev.next = first
  else : result = first
  
  return result


def reverse_k_nodes(head, k) :
  
  prev,curr,next_node = None, head, None

  res_last_node = None
  i = 0

  while curr and i <= k :
    if res_last_node is None :
      res_last_node = curr

    next_node = curr.next
    curr.next = prev
    prev = curr
    curr = next_node

    i += 1
  
  res_first_node = prev

  res_last_node.next = curr

  return res_first_node


def find_len(head) :
  count = 0
  start = head

  while start :
    count += 1
    start = start.next
  
  return count
  





