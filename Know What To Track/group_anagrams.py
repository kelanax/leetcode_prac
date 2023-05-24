'''

Given a list of words or phrases, group the words that are anagrams of 
each other. An anagram is a word or phrase formed from another word by 
rearranging its letters.

-------------------------------
PATTERN: KNOWING WHAT TO TRACK
-------------------------------

'''





def group_anagrams(strs):
    
    if not strs : return [[]]
    
    result = []
    ana = {}
    a = ord('a')

    for word in strs :
        char_list = [0] * 26
        for c in word : 
            c = c.lower()
            char = ord(c) - a

            char_list[char] += 1
        
        input_tuple = tuple(char_list)
        if input_tuple in ana : ana[input_tuple].append(word)
        else : ana[input_tuple] = [word]

    for k,v in ana.items() :
        result.append(v)

    return result














