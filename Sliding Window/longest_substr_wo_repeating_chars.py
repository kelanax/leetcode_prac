'''

PROBLEM: 

Given a string, str, return the length of the longest substring without repeating characters.

-------------------------
PATTERN: SLIDING WINDOW  
-------------------------

'''

def find_longest_substring(str):
   
   if len(str) == 1 : return 1
   if len(str) == 0 : return 0

   locs = {str[0] : 0}
   left, right = 0, 1
   longest_str = 1

   while right < len(str) :

      if str[right] in locs and locs[str[right]] >= left :
         if right - left > longest_str : 
            longest_str = right - left
         left = locs[str[right]] + 1
         locs[str[right]] = right
         right += 1
      else :
         locs[str[right]] = right
         right += 1

   if right - left > longest_str : 
      longest_str = right - left

   return longest_str

