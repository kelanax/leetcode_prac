'''

PROBLEM: 

You’re given a list containing the schedules of multiple people. Each person’s schedule 
is a list of non-overlapping intervals in sorted order. An interval is specified with the 
start time and the end time, both being positive integers. Your task is to find the list 
of intervals representing the free time for all the people. We’re not interested in the 
interval from negative infinity to zero or from the end of the last scheduled interval 
in the input to positive infinity.

-------------------------
PATTERN: MERGE INTERVALS 
-------------------------

'''


# from interval import Interval

def employee_free_time(schedule):  

    result = []
    prev_max_end = float('-inf')
     
    sched = [interval for employee in schedule for interval in employee]
    sched.sort(key=lambda interval: interval.start)

    for i in range(len(sched) - 1) :

        if sched[i].end >= sched[i+1].start : 
            prev_max_end = max(prev_max_end, sched[i].end)
            continue
        else : 
            result.append(Interval(max(sched[i].end, prev_max_end), sched[i+1].start))

    return result




# SOURCE CODE FROM QUESTION
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.closed = True  # by default, the interval is closed
    # set the flag for closed/open

    def set_closed(self, closed):
        self.closed = closed

    def __str__(self):
        return "[" + str(self.start) + ", " + str(self.end) + "]" \
            if self.closed else \
                "(" + str(self.start) + ", " + str(self.end) + ")"




