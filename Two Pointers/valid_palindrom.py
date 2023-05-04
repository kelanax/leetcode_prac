'''
PROBLEM: 
Write a function that takes a string as input and checks whether it can be a 
valid palindrome by removing at most one character from it.

----------------------
PATTERN: TWO POINTERS
----------------------

'''




def is_palindrome(s):
  # Write your code here
  # Tip: You may use the code template provided
  # in the two_pointers.py file
  left = 0
  right = len(s) - 1
  return palin_helper(s, left, right, False)


def palin_helper(s, left, right, has_skipped) :

  if left >= right : return True

  if s[left] == s[right] : return palin_helper(s, left+1, right-1, has_skipped)
  elif not has_skipped : 
    if palin_helper(s, left+1, right, True) : return True
    else : return palin_helper(s, left, right-1, True)
  else : return False
