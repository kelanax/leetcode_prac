'''

Given an array, nums, containing n distinct numbers in the range [0,n], 
return the only number in the range that is missing from the array.

----------------------
PATTERN: CYCLIC SORT
----------------------

'''










from traversal import *


# Tip: You may use some of the code templates provided
# in the support file

def find_missing_number(nums):
  
  i = 0
  length = len(nums)
  while i < length :

    val = nums[i]

    if val >= length : i += 1
    elif val != nums[val] : 
      nums[i], nums[val] = nums[val], nums[i]
    else : i += 1

  for i in range(length) :
    if nums[i] != i : return i

  return length




# def find_missing_number(nums):
#   len_nums = len(nums)
#   index = 0
 
#   while index < len_nums:

#     value = nums[index]

#     if value < len_nums and value != nums[value]:
#       nums[index], nums[value] = nums[value], nums[index]

#     elif value >= len_nums:
#       index+=1

#     else:
#       index += 1

#   for x in range(len_nums):
#     if x != nums[x]:
#       return x
#   return len_nums











