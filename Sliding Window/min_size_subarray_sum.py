'''

PROBLEM: 

Given an array of positive integers nums and a positive integer target, find the 
window size of the shortest contiguous subarray whose sum is greater than or equal 
to the target value. If no subarray is found, 0 is returned.

-------------------------
PATTERN: SLIDING WINDOW  
-------------------------

'''



def min_sub_array_len(target, nums):
    
    total = 0
    min_len = float('inf')
    left = right = 0

    while right < len(nums) :

        # if nums[right] == target : return 1

        total += nums[right]
        while total >= target and left <= right :
            if total - nums[left] >= target : 
                total -= nums[left]
                left += 1      
            else :
                if right - left + 1 < min_len :
                    min_len = right - left + 1
                break
        right += 1
 

    return min_len if min_len != float('inf') else 0




