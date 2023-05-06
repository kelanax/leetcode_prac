'''

PROBLEM: 

We are given an input array of meeting time intervals, intervals, where each interval 
has a start time and an end time. Your task is to find the minimum number of meeting 
rooms required to hold these meetings.

-------------------------
PATTERN: MERGE INTERVALS 
-------------------------

'''


from interval import Interval
import heapq

def find_sets(intervals):
    
    if len(intervals) == 0 : return 0
    if len(intervals) == 1 : return 1

    intervals.sort(key=lambda x : x.start)

    h = [intervals[0].end]
    heapq.heapify(h)
    i = 0

    for inter in intervals :
        if i == 0 : 
            i += 1
            continue        
        
        if inter.start >= h[0] :
            heapq.heappop(h)
            heapq.heappush(h, inter.end)
        else : 
            i += 1
            heapq.heappush(h, inter.end)

    return i

















