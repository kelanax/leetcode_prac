'''

PROBLEM: 

The latest version of a software product fails the quality check. Since each version is developed 
upon the previous one, all the versions created after a bad version are also considered bad. 
Suppose you have n versions with the IDs [1,2,...,n] , and you have access to an API function that
returns TRUE if the argument is the ID of a bad version. Your task is to find the first bad version, 
which is causing all the later ones to be bad. You have to implement a solution with the minimum number
of API calls.

---------------------------------
PATTERN: MODIFIED BINARY SEARCH
---------------------------------

'''


from api import *

version_api = api(0)

def is_bad_version(v):
    return version_api.is_bad(v)

def first_bad_version(n):
# -- DO NOT CHANGE THIS SECTION
    version_api.n = n
# -- 

    # Write your code here:

    first, last = 1 , n

    first_version = -1
    num_calls = 0
    
    while first <= last :

        mid = (first + last) // 2
        if is_bad_version(mid) :
            num_calls += 1
            first_version = mid
            last = mid - 1
        else : 
            first = mid + 1

    return first_version, num_calls


   





