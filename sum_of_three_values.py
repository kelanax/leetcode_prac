"""
PROBLEM: 
Sum of Three Values
Given an array of integers, nums, and an integer value, target, determine if there are any 
three integers in nums whose sum is equal to the target, that is, nums[i] + nums[j] + nums[k] == target. 
Return TRUE if three such integers exist in the array. Otherwise, return FALSE.

Note: A valid triplet consists of elements with distinct indexes. This means, for 
the triplet nums[i], nums[j], and nums[k], i ≠ j, i ≠ k and j ≠ k.
"""

def find_sum_of_three(nums, target):
   # Replace this placeholder return statement with your code

   nums_sorted = nums.copy()
   nums_sorted.sort()
   
   for i in range(len(nums_sorted) - 2) :

      left = i + 1
      right = len(nums_sorted) - 1
      while left < right :
         sum = nums_sorted[i] + nums_sorted[left] + nums_sorted[right]

         if ( sum == target) : return True
         elif sum < target : left += 1
         else : right -= 1

   return False


