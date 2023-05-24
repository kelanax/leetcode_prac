'''

PROBLEM: 

Given two strings, str1 and str2, find the index of the extra character 
that is present in only one of the strings.

---------------------------
PATTERN: BIT MANIPULATION
---------------------------

'''



def extra_character_index(str1, str2):
    
    result = 0
    count = 0
    
    for c in str1 :
        result = (result) ^ ((ord)(c))

    for c in str2 :
        result = (result) ^ ((ord)(c))

    length = max(len(str1), len(str2))
    string = str1 if len(str1) > len(str2) else str2
    
    for index, c in enumerate(string) :
        if c == ((chr)(result)) : return index


    return -1






