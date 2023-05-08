'''

PROBLEM: 

You’re given a linked list. Your task is to reverse all of the nodes that are present 
in the groups with an even number of nodes in them. The nodes in the linked list are 
sequentially assigned to non-empty groups whose lengths form the sequence of the natural 
numbers ( 1 , 2 , 3 , 4... ) (1,2,3,4...) . The length of a group is the number of nodes 
assigned to it. In other words: 

- The 1 st node is assigned to the first group. 
- The 2 nd and 3 rd nodes are assigned to the second group. 
- The 4 th ,  5 th , and  6 th nodes are assigned to the third group and so on. 
You have to return the head of the modified linked list.

Note: The length of the last group may be less than or equal to 1 + the length of the 
second to the last group
--------------------------------------------
PATTERN: IN PLACE REVERSAL OF A LINKED LIST 
--------------------------------------------

'''








# from linked_list import LinkedList

def reverse_even_length_groups(head):
  
  node = prev = head
  duration = count = 1
  start = end = tail = None
  

  while node :
    if duration % 2 == 1 and count != duration:
      if not start : start = prev
      prev = node
      node = node.next
      count += 1 
      continue
    
    if duration % 2 == 0 and count != duration :
      if not start : start = prev
      prev = node
      node = node.next
      count += 1 
      continue


    if count == duration :
      prev_temp = node
      end = node.next if node else None
      if duration % 2 == 0 :
        prev, start, end = start, start.next, node.next
  
        while start != end :
          if not tail : tail = start
          next_node = start.next
          start.next = prev.next
          prev.next = start
          start = next_node
        if tail : 
          tail.next = end

      duration += 1
      count = 1
      prev = prev_temp
      node = end
      start = end = tail = None

  if count > 2 and (count - 1) % 2 == 0 :
    while count > 1 :
      prev = start
      start = start.next
      count -= 1
    end = start

    prev.next = None
    while end :
      next_node = end.next
      end.next = prev.next
      prev.next = end
      end = next_node



  return head










