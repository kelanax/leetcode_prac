'''

PROBLEM: 

Given two sorted integer arrays, nums1 and nums2 , and the number of data elements in 
each array, m and n , implement a function that merges the second array into the first one. 
You have to modify nums1 in place.

----------------------
PATTERN: K-WAY MERGE
----------------------

'''



def merge_sorted(nums1, m, nums2, n):
    
    ptr1 = m - 1
    ptr2 = n - 1
    curr = m + n - 1

    while ptr1 >= 0 and ptr2 >= 0 :
        if nums1[ptr1] >= nums2[ptr2] :
            nums1[curr] = nums1[ptr1]
            ptr1 -= 1
        else :
            nums1[curr] = nums2[ptr2]
            ptr2 -= 1
        curr -= 1

    while ptr2 >= 0 :
        nums1[curr] = nums2[ptr2]
        ptr2 -= 1
        curr -= 1
    

    return nums1



