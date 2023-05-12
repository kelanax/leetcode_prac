'''

PROBLEM: 

Given an input string, return all possible permutations of the string. 
Note: The order of permutations does not matter.

------------------
PATTERN: SUBSETS
------------------

'''


def permute_word(word):
    result = []

    helper(word, 0, result)
    
    return result


def helper(word, index, result) :

    if index == len(word) - 1 :
        result.append(word)
        return
    
    for i in range(index, len(word)) :

        li = list(word)
        li[index], li[i] = li[i], li[index]
        new_word = "".join(li)

        helper(new_word, index + 1, result) 



