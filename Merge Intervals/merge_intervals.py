'''

PROBLEM: 

We are given an array of closed intervals, intervals, where each interval has a start time 
and an end time. The input array is sorted with respect to the start times of each interval. 
For example, intervals = [ [1,4], [3,6], [7,9] ]
 is sorted in terms of start times 1,3, and 7.

Your task is to merge the overlapping intervals and return a new output array consisting of 
only the non-overlapping intervals.

-------------------------
PATTERN: MERGE INTERVALS 
-------------------------

'''


def merge_intervals(intervals):

    res = []

    for i, interval in enumerate(intervals) :         
        if i == 0 : 
            res.append(interval)
            continue
        last = res[len(res) - 1]

        if do_intervals_overlap(res[len(res) - 1], interval) :
            res[len(res) - 1].end = max(res[len(res) - 1].end, interval.end)
        else : res.append(interval)
    
    return res
        

def do_intervals_overlap(interval_1, interval_2) :
    return interval_2.start >= interval_1.start and interval_2.start <= interval_1.end

def merge(interval_1, interval_2) :
    return [min(interval_1.start, interval_2.start), max(interval_1, i.endnterval_2.end)]

    

    

