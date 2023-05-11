'''

PROBLEM: 

Given a sorted integer array nums and two integers—k and num—return the k closest integers to 
num in this array. Ensure that the result is sorted in ascending order. The integer a is closer 
to num than an integer b if the following are true: |a - num| < < |b - num|, or |a - num| = = |b - num| 
and a < < b

---------------------------------
PATTERN: MODIFIED BINARY SEARCH
---------------------------------

'''



def find_closest_elements(nums, k, num):

    if len(nums) <= k : return nums

    res = []
    low , high = 0 , len(nums) - 1
    mid = (low + high) // 2

    while low < high - 1 :
        
        mid = (low + high) // 2

        if nums[mid] == num :
            low = mid
            break
        elif num < nums[mid] :
            high = mid - 1
        else :
            low = mid + 1
    

    left, right = low, low + 1
    

    for _ in range(k) :
        if left == -1 :
            right += 1
            continue
        if right == len(nums) :
            left -= 1
            continue

        l_dist = abs(nums[left] - num)
        r_dist = abs(nums[right] - num)

        if l_dist <= r_dist:
            left -= 1
        elif r_dist < l_dist : 
            right += 1


    res = nums[left + 1 : right]


    return res







