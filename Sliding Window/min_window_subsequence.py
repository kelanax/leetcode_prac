'''

PROBLEM: 

Given strings str1 and str2, find the minimum (contiguous) substring sub_str of str1, 
such that every character of str2 appears in sub_str in the same order as it is present in str2.

If there is no window in str1 that covers all characters in str2, return an empty string.

If there are multiple minimum-length windows, return the one with the leftmost starting index.

-------------------------
PATTERN: SLIDING WINDOW  
-------------------------

'''




def min_window(str1, str2):
    
    if len(str1) < len(str2) : return ""

    str1_i = str2_i = start = next_char = 0
    first_char = str2[0]

    min_substring = ""
    min_len = float('inf')

    while str1_i < len(str1) :

        str2_i = 0

        while next_char < len(str1) and str1[next_char] != first_char :
            next_char += 1
        if next_char == len(str1) - 1 : return min_substring

        start = str1_i = next_char
        next_char += 1

        while str1_i < len(str1) and str2_i < len(str2) :
            if str1[str1_i] == str2[str2_i] :
                str1_i += 1
                str2_i += 1
            else : str1_i += 1
        if str1_i >= len(str1) - 1 and str2_i < len(str2) : return min_substring

        sub_len = str1_i - start
        if sub_len < min_len :
            min_substring = str1[start:str1_i]
            min_len = sub_len
        


    return min_substring







