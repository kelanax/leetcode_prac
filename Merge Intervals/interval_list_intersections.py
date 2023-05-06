'''

PROBLEM: 

For two lists of closed intervals given as input, interval_list_a and interval_list_b, 
where each interval has its own start and end time, write a function that returns the 
intersection of the two interval lists.

For example, the intersection of [3,8] and [5,10] is [5,8].

-------------------------
PATTERN: MERGE INTERVALS 
-------------------------

'''


from interval import Interval

# Function to find the intersecting points between two intervals
def intervals_intersection(interval_list_a, interval_list_b):
    
    output = []
    if len(interval_list_a) == 0 or len(interval_list_b) == 0 : return output

    i = 0
    b_size = len(interval_list_b)
    b = interval_list_b[i]

    for list_a in interval_list_a :

        a_start, a_end = list_a.start, list_a.end
        
        while b.start > a_end or b.end < a_start :
            if b.start > a_end : break
            i += 1
            if i < b_size : b = interval_list_b[i]
            else : break

        if b.start > a_end : continue

        if (b.start >= a_start and b.start <= a_end) or (a_start >= b.start and a_start <= b.end) :
            merged = merge(list_a, b)
            output.append(merged)


    return output


def merge(inter1, inter2) :
    left = max(inter1.start, inter2.start)
    right = min(inter1.end, inter2.end)

    return Interval(left,right)


