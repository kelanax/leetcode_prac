'''

PROBLEM: 

You are required to find an integer t in an array arr of non-distinct integers. Prior to being 
passed as input to your search function, arr has been processed as follows: It has been sorted 
in non-descending order. It has been rotated around some pivot k , such that, after rotation, 
it looks like this: [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]. 

For example, [10, 30, 40, 42, 42, 47, 78, 90, 901], rotated around pivot k=5 
becomes [47, 78, 90, 901, 10, 30, 40, 42, 42]. Return TRUE if t exists in the rotated, 
sorted array arr, and FALSE otherwise, while minimizing the number of operations in the 
search.

---------------------------------
PATTERN: MODIFIED BINARY SEARCH
---------------------------------

'''




def search(arr, t):

    low , high = 0 , len(arr) - 1
    mid = 0

    while low <= high : 
        mid = (low + high) // 2

        if arr[mid] == t : return True

        if arr[mid] <= arr[high] :
            if t > arr[mid] and t <= arr[high] :
                low = mid + 1
            else : high = mid - 1
        else :
            if t >= arr[low] and t < arr[mid] : 
                high = mid - 1 
            else : low = mid + 1

    return False


