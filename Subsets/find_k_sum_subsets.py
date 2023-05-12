'''

PROBLEM: 

Given a set of n positive integers, find all the possible subsets of integers that sum up 
to a number k.

------------------
PATTERN: SUBSETS
------------------

'''


def get_bit(num, bit) :
  temp = (1 << bit)
  if (temp & num) == 0 : return False
  else : return True

def get_k_sum_subsets(set_of_integers, target_sum):
  
  length = len(set_of_integers)
  if length == 0 : return []

  all_subsets = []
  result = []
  n = 2**(length)

  for i in range(n) :
    curr_set = set()
    for j in range(length) :
      if get_bit(i,j) :
        curr_set.add(set_of_integers[j])
    
    if i == 0 : all_subsets.append([])
    else : all_subsets.append(list(curr_set))


  for subset in all_subsets :
    total = sum(subset)
    if total == target_sum : result.append(subset)



  return result  






