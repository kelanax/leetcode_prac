'''

PROBLEM: 

Given a string, s, that represents a DNA sequence, and a number, k, return all the contiguous 
sequences (substrings) of length k that occur more than once in the string. The order of the 
returned subsequences does not matter. If no repeated subsequence is found, the function 
should return an empty set.

-------------------------
PATTERN: SLIDING WINDOW  
-------------------------

'''



def find_repeated_sequences(s, k):
    
    if k >= len(s) : return set()

    substrings = set()
    output = set()

    start = 0
    end = start + k

    while start <= len(s) - k  :
   
        new_str = s[start:end]

        if new_str in substrings : 
            output.add(new_str)
        else : 
            substrings.add(new_str)

        start += 1
        end = start + k

    return output

