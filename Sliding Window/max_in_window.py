'''

PROBLEM: 

Given an integer list, nums, find the maximum values in all the contiguous subarrays (windows) 
of size w.

-------------------------
PATTERN: SLIDING WINDOW  
-------------------------

'''



def find_max_sliding_window(nums, w):

    start = 0
    end = 0 + w if w <= len(nums) else len(nums) - 1
    old_max = float('-inf')

    output = []

    while start <= len(nums) - w :
        if start == 0 :
            old_max = max(nums[start:end])
            output.append(old_max)
        else : 
            removed_val = nums[start - 1]
            added_val = nums[end - 1]
            if removed_val != old_max and added_val > old_max : 
                old_max = added_val
                output.append(added_val)
            elif removed_val != old_max and added_val <= old_max : 
                output.append(old_max)
            else :
                max_val = max(nums[start:end])
                old_max = max_val
                output.append(max_val)
        
        start += 1
        end = start + w


    
    return output


