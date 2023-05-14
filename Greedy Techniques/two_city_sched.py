'''

PROBLEM: 

A company is planning to interview 2n people. You're given the array costs where 
costs[i]=[aCosti ,bCost i] . The cost of flying the ith person to city A is Cost i, and 
the cost of flying the ith person to city B is Cost i . 

Return the minimum cost to fly every person to a city such that exactly n n people arrive 
in each city.

---------------------------
PATTERN: GREEDY TECHNIQUES
---------------------------

'''



def two_city_scheduling(costs):

  # costs.sort(key= lambda x: x[0])

  diff = []
  total = 0
  for cost in costs :
    difference = cost[0] - cost[1]
    val = [difference, cost[0], cost[1]]
    diff.append(val) 

  diff.sort(key= lambda x: x[0])
  print("cost:", cost)
  print("diff:", diff)

  length = len(diff) 

  for i in range(length) :

    if i < (length // 2) :
      total += diff[i][1]
    else : total += diff[i][2]




  return total





