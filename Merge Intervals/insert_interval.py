'''

PROBLEM: 

You’re given a list of non-overlapping intervals, and you need to insert another interval 
into the list. Each interval is a pair of non-negative numbers, the first being the start 
time and the second being the end time of the interval. The input list of intervals is 
sorted in ascending order of start time.

The intervals in the output must also be sorted by the start time, and none of them should 
overlap. This may require merging those intervals that now overlap as a result of the 
addition of the new interval.

-------------------------
PATTERN: MERGE INTERVALS 
-------------------------

'''


from interval import *

def insert_interval(existing_intervals, new_interval) :
  output = []
  start = new_interval.start
  end = new_interval.end
  has_been_inserted = False

  for inter in existing_intervals :

    res = None

    if start < inter.start and end < inter.start : 
      res = inter
    elif start > inter.end : 
      res = inter
    elif (start >= inter.start and start <= inter.end) or (inter.start >= start and inter.start <= end):
      res = merge(inter, new_interval)
      has_been_inserted = True
    
    # insert into output
    if len(output) == 0 : output.append(res)
    else:
      last = output[len(output) - 1]

      if res.start > last.end :
        output.append(res)
      else :
        merged = merge(last, res)
        output[len(output) - 1] = merged
  
  if not has_been_inserted : output.append(new_interval)


  return output



def merge(inter1, inter2) :
  left = min(inter1.start, inter2.start)
  right = max(inter1.end, inter2.end)

  return Interval(left,right)



