'''

PROBLEM: 

For a given number, n, generate all combinations of balanced parentheses.

------------------
PATTERN: SUBSETS
------------------

'''


def generate_combinations(n):
    
    results = []

    helper([], 0, 0, n, results)

    return results


def helper(curr_path, left, right, n, results) :

    if left == right and left == n :
        valid = "".join(curr_path)
        results.append(valid)
        return
    
    opt = ["(", ")"]
    for i in range(2) :
        if i == 0 :
            if left < n :
                curr_path.append(opt[i])
                helper(curr_path, left + 1, right, n, results)
                curr_path.pop()
        else :
            if left > 0 and right + 1 <= left :
                curr_path.append(opt[i])
                helper(curr_path, left, right + 1, n, results)
                curr_path.pop()         
        





