'''

PROBLEM: 

Given an integer n , we need to calculate the 32-bit unsigned integer it 
would be if we reversed its bits. When we say “reverse” we don't mean 
flipping the 0s to 1s and vice versa, but simply reversing the order 
in which they appear - from left-to-right to right-to-left. We need to 
return the integer the reversed bits result in.

---------------------------
PATTERN: BIT MANIPULATION
---------------------------

'''




def reverse_bits(n):
    # n = '{:032b}'.format(n) will convert n into a binary number
    # n = int(n, 2) will convert n into an integer from 32-bit binary
    # Write your code here

    limit = 32
    result = 0

    for i in range(limit) :

        if n & 1 :
            result = result << 1
            result = result ^ 1
        else :
            result = result << 1
        
        n = n >> 1

    return result






