'''

PROBLEM: 

We are given two strings, s and t. The minimum window substring of t in s is defined as follows:

- It is the shortest substring of s that includes all of the characters present in t.
- The frequency of each character in this substring that belongs to t should be equal to or greater 
  than its frequency in t.
- The order of the characters does not matter here.

We have to find the minimum window substring of t in s.

-------------------------
PATTERN: SLIDING WINDOW  
-------------------------

'''


def min_window(s, t):

    if len(s) < len(t) : return ""

    i = start = 0
    freq_dict = create_freq_dict(t)
    
    min_str = ""
    min_len = float('inf')

    while start < len(s) :

        if len(s) - start < len(t) : return min_str
        counts = initialize_freq_dict(t)
        total = len(t)

        i = start
        while i < len(s) and total > 0 :
            if s[i] in freq_dict and counts[s[i]] < freq_dict[s[i]] :
                counts[s[i]] = counts[s[i]] + 1
                total -= 1
            i += 1
        
        if i >= len(s) and total > 0 : return min_str
        elif i - start < min_len :
            min_str = s[start:i]
            min_len = i - start

        start += 1



    return min_str




def initialize_freq_dict(string) :

    freq_dict = {}

    for char in string :
        if char not in freq_dict :
            freq_dict[char] = 0

    return freq_dict


def create_freq_dict(string) :

    freq_dict = {}

    for char in string :
        if char in freq_dict :
            val = freq_dict[char]
            val += 1
            freq_dict[char] = val
        else :
            freq_dict[char] = 1

    return freq_dict







