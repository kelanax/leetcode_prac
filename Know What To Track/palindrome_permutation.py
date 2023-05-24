'''

For a given string, find whether or not a permutation of this string is a 
palindrome. You should return TRUE if such a permutation is possible and 
FALSE if it isn’t possible.

-------------------------------
PATTERN: KNOWING WHAT TO TRACK
-------------------------------

'''



from populating_hashmap import *

# Tip: You may use some of the code templates provided
# in the support files

def permute_palindrome(st):
  freq = {}

  for char in st :
    freq[char] = freq.get(char, 0) + 1
  
  found_odd_count = False
  for letter,count in freq.items() :
    if count&1 :
      if found_odd_count : return False
      else : found_odd_count = True

  return True


