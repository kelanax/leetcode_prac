'''

PROBLEM: 

You're given two sorted integer arrays, nums1 and nums2, of size m and n, respectively. 
Your task is to return the median of the two sorted arrays. 
- The overall run time complexity should be O(log(m+n)).

----------------------
PATTERN: K-WAY MERGE
----------------------

'''


def find_median(nums1, nums2):
    
    # print("hey")
    A = nums1 if len(nums1) >= len(nums2) else nums2
    B = nums1 if len(nums1) < len(nums2) else nums2

    total_len = len(nums1) + len(nums2)
    isEven = total_len % 2 == 0
    half = total_len // 2


    start , end = 0, len(A) - 1
    median = 0

    # while start <= end :
    for _ in range(2) :

        A_mid = (start + end) // 2
        B_mid = half - A_mid - 2

        Aleft = A[A_mid] if A_mid >= 0 else float("-inf")
        Aright = A[A_mid + 1] if (A_mid + 1) < len(A) else float("inf")
        Bleft = B[B_mid] if B_mid >= 0 else float("-inf")
        Bright = B[B_mid + 1] if (B_mid + 1) < len(B) else float("inf")

        

        if Aleft <= Bright and Bleft <= Aright :
            if (Aright == float("inf") and Bright == float("inf")) or (Aleft == float("-inf") and Bleft == float("-inf")) :
                break
            if isEven :
                val1 = max(Aleft, Bleft)
                val2 = min(Aright, Bright)
                median = (val1 + val2) / 2
                return median
            else :
                return min(Aright, Bright)

        elif Aleft > Bright :
           end = A_mid - 1
        else : start = A_mid + 1
            


    return median


    



