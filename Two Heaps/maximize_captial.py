'''

PROBLEM: 

You need to develop a program for making automatic investment decisions for a busy investor. 
The investor has some start-up capital, c , to invest and a portfolio of projects in which 
they would like to invest in. The investor wants to maximize their cumulative capital as a 
result of this investment. 

To help them with their decision, they have information on the 
capital requirement for each project and the profit it’s expected to yield. For example, 
if project A has a capital requirement of 3 3 , and the investor’s current capital is 1 1 , 
then the investor can’t invest in this project. On the other hand, if the capital requirement 
of a project B is 1 1 , then the investor can invest in this project. Now, supposing that the 
project yields a profit of 2 2 , the investor’s capital at the end of the project will 
be 1 + 2 = 3 1+2=3 . The investor can now choose to invest in project A as well since their 
current capital has increased. 

As a basic risk-mitigation measure, the investor would like 
to set a limit on the number of projects, k, they invest in. For example, if the value of 
k is 2, then we need to identify the two projects that the investor can afford to invest in, 
given their capital requirements, and that yield the maximum profits. 

Further, these are 
one-time investment opportunities, that is, the investor can only invest once in a given 
project.

--------------------
PATTERN: TWO HEAPS
--------------------

'''



import heapq
# from min_heap import *
# from max_heap import *


def maximum_capital(c, k, capitals, profits):
  
  min_capitals = [[item[1], profits[item[0]]] for item in enumerate(capitals)]
  heapq.heapify(min_capitals)
  
  max_profits = []
  heapq.heapify(max_profits)

  cap = c

  while k > 0 :
    profit = 0
    while min_capitals and min_capitals[0][0] <= cap :
      project = heapq.heappop(min_capitals)
      heapq.heappush(max_profits, (-project[1]))

    if max_profits : profit = -heapq.heappop(max_profits)

    cap += profit
    k -= 1

  return cap
 


