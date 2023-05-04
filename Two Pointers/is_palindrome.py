''' 
PROBLEM: 
Write a function that takes a string s as input and checks whether it’s a palindrome or not.

----------------------
PATTERN: TWO POINTERS
----------------------

'''

def is_palindrome(s):
  # Write your code here
  # Tip: You may use the code template provided
  # in the two_pointers.py file
  if len(s) <= 1 : return True

  left_index = 0
  right_index = len(s) - 1

  while left_index < right_index : 
    if s[left_index] != s[right_index] : return False
    
    left_index += 1
    right_index -= 1

  return True

