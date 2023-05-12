'''

PROBLEM: 

Given a string having digits from 2 - 9 inclusive, return all the possible letter combinations 
that can be made from the numbers in the string. Return the answer in any order. 
A mapping of digits to letters is given below. 

Note: 1 doesn't map to any letter.

------------------
PATTERN: SUBSETS
------------------

'''











'''
# PRODUCES WRONG ORDER:

import copy
def letter_combinations(digits):
    
    if len(digits) == 0 : return []
    num_dict = {"1":"", "2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
    options = []
    result = []

    if len(digits) == 1 :
        return [x for x in num_dict[digits[0]]]
    
    for digit in digits : 
        word = num_dict[digit]
        options.append(list(word))
    
    print("options:", options)
    
    helper(options,0,result)

    return result



def helper(options, index, result) :

    if index == len(options) - 1:
        for char in options[index] :
            # print("char:", char)
            result.append(char)
        print("result:", result)
        return
    
    helper(options, index + 1, result)
    length = len(result)
    # li = copy.deepcopy(result)
    
    for i in range(len(options[index])) :
        li = []
        # if i == (len(options[index]) - 1) : li = result
        # else : li = copy.deepcopy(result)

        for j in range(length) :
            word = list(result[j])
            # word = result[j]
            word.append(options[index][i])
            # result[j] = "".join(word)
            # result.append("".join(word))
            if i != (len(options[index]) - 1) : 
                # result.append("".join(word))
                # result.append(result)
                result.append("".join(word))
            else : result[j] = "".join(word)
            
            if j == length : return



'''


