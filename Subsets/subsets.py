'''

PROBLEM: 

Given a set of integers, find all possible subsets within the set. Note: The solution set 
must not contain duplicate subsets. Return the solution in any order.

------------------
PATTERN: SUBSETS
------------------

'''



import copy
def find_all_subsets(v):

    n = 2**(len(v))
    res = [[]]
    # mask = [0] * len(v)
    i = 0

    while len(res) < n :
        current_subset = copy.deepcopy(res)
        # start = ((len(res)) // 2)

        for j in range(len(current_subset)) :
            current_subset[j].append(v[i])
        i += 1
        res = res + current_subset

    return res






#################################################

# THEIR SOLUTION :

'''

def get_bit(num, bit):
    temp = (1 << bit)
    temp = temp & num
    if temp == 0:
        return 0
    return 1

def find_all_subsets(v):
    sets = []
    
    if not v:
        return [[]]
    else:
        subsets_count = 2 ** len(v)
        for i in range(0, subsets_count):
            st = set()
            for j in range(0, len(v)):
                if get_bit(i, j) == 1 and v[j] not in st:
                    st.add(v[j])
            
            if i == 0:
                sets.append([])
            else:
                sets.append(list(st))
    return sets


'''


