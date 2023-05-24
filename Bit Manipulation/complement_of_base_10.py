'''

PROBLEM: 

For any n positive number in base 10, return the complement of its 
binary representation as an integer in base 10.

---------------------------
PATTERN: BIT MANIPULATION
---------------------------

'''



from math import floor, log2

def find_bitwise_complement(num):
  
    bit_count = floor(log2(num)) + 1
    # computing the all bits set of the number
    all_bits_set = pow(2, bit_count) - 1
    # flipping all bits of number by taking xor with all_bits_set
    return num ^ all_bits_set








