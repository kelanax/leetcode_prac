'''

PROBLEM: 

Given a sorted integer array, nums, and an integer value, target, the array is rotated by 
some arbitrary number. Search and return the index of target in this array. If the target 
does not exist, return -1.

---------------------------------
PATTERN: MODIFIED BINARY SEARCH
---------------------------------

'''


def binary_search_rotated(nums, target):

  low, high = 0, len(nums) - 1
  # mid = len(nums) // 2

  while low <= high :
    mid = (high + low) // 2  # Remeber to use parentheses because of operator precedence
    if nums[mid] == target : return mid

    if nums[low] <= nums[mid] :
      if nums[low] <= target and target < nums[mid] :
        high = mid - 1
      else :
        low = mid + 1
    else :
      if nums[mid] < target and target <= nums[high] :
        low = mid + 1
      else :
        high = mid - 1

  return -1




