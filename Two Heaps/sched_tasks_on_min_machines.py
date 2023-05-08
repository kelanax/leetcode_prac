'''

PROBLEM: 

Given a set of n number of tasks, implement a task scheduler method, tasks(), 
to run in O(n logn) time that finds the minimum number of machines required to 
complete these n tasks.

--------------------
PATTERN: TWO HEAPS
--------------------

'''


import heapq


def tasks(tasks_list):

    heapq.heapify(tasks_list)
    machines = []

    while tasks_list :

        task = heapq.heappop(tasks_list)

        if machines and machines[0] <= task[0] :
            heapq.heappop(machines)
            heapq.heappush(machines, task[1])
        else: heapq.heappush(machines, task[1])



    return len(machines)














