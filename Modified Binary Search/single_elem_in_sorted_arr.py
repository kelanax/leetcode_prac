'''

PROBLEM: 

In this problem, you’re given an array of sorted integers in which all of the integers, except one, 
appears twice. Your task is to find the single integer that appears only once. The solution should 
have a time complexity of O(logn) or better and a space complexity of O(1).

---------------------------------
PATTERN: MODIFIED BINARY SEARCH
---------------------------------

'''




def single_non_duplicate(nums): 

  left , right = 0 , len(nums) - 1
  mid = 0

  while left < right :
    mid = (left + right ) // 2
    if (mid % 2) == 1 : mid -= 1

    if mid >= 1 and mid <= len(nums) - 2 :
      if nums[mid] != nums[mid + 1] and nums[mid] != nums[mid - 1] :
        return nums[mid] 
    if nums[mid] == nums[mid + 1] : left = mid + 2
    elif nums[mid] != nums[mid + 1] : right = mid

  return nums[left]


