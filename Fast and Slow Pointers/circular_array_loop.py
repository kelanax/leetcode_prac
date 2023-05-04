'''
An input array, nums containing non-zero integers, is given, where the value at each index 
represents the number of places to skip forward (if the value is positive) or 
backward (if the value is negative). When skipping forward or backward, wrap around if you 
reach either end of the array. For this reason, we are calling it a circular array. 
Determine if this circular array has a cycle. A cycle is a sequence of indices in the 
circular array characterized by the following:

- The same set of indices is repeated when the sequence is traversed in accordance with the 
  aforementioned rules.
- The length of the sequence is at least two.
- The loop must be in a single direction, forward or backward.


--------------------------------
PATTERN: FAST AND SLOW POINTER
--------------------------------

'''





def circular_array_loop(nums):  

    # Write your code here
    slow, fast = 0, 0
    size = len(nums)
   

    for i in range(size) : 
        
        has_changed_dir = False
        fast_dir, slow_dir = 0, 0
        slow, fast = i, i
        slow_dir = 1 if nums[slow] > 0 else -1
        fast_dir = slow_dir

        # take first step(s) for fast and slow

        while not has_changed_dir :
            
            prev_slow = slow
            slow = correct_index(slow, nums[slow], size)
            print("prev_slow:", prev_slow, ", slow:", slow)
            if nums[slow] < 0 and slow_dir > 0 or nums[slow] > 0 and slow_dir < 0 :
                has_changed_dir = True
                break
            elif prev_slow == slow : break
            

            num_fast_moves = 2

            for _ in range(num_fast_moves) :
                prev_fast = fast
                fast = correct_index(fast, nums[fast], size)

                if nums[fast] < 0 and fast_dir > 0 or nums[fast] > 0 and fast_dir < 0 :
                    has_changed_dir = True
                    break 
                elif prev_fast == fast : break

            if not prev_fast == fast :
                if fast == slow : return True
        

    return False


def correct_index(i, num_steps, size) :
    
    new_index = (i + num_steps) % size

    while new_index < 0 :
        new_index += size
    
    return new_index
    




















# OLD CODE: -----------------------------------------------------------------------------
def circular_array_loop(nums):  

    # Write your code here
    slow, fast = 0, 0
    size = len(nums)

    print("size:", size)
    print("size % size:", size % size)
   

    for i in range(size) : 
        
        has_changed_dir = False
        fast_dir, slow_dir = 0, 0
        slow, fast = i, i
        slow_dir = 1 if nums[slow] > 0 else -1
        fast_dir = slow_dir

        # take first step(s) for fast and slow

        while not has_changed_dir :
            
            prev_slow = slow
            slow = correct_index(slow + nums[slow], slow, size)
            if nums[slow] < 0 and slow_dir > 0 or nums[slow] > 0 and slow_dir < 0 :
                has_changed_dir = True
                break
            elif prev_slow == slow : break
            
            prev_fast = fast
            fast = correct_index(fast + nums[fast], fast, size)
            if nums[fast] < 0 and fast_dir > 0 or nums[fast] > 0 and fast_dir < 0 :
                has_changed_dir = True
                break 
            elif prev_fast == fast : break
            
            prev_fast = fast
            fast = correct_index(fast + nums[fast], fast, size)

            if nums[fast] < 0 and fast_dir > 0 or nums[fast] > 0 and fast_dir < 0 :
                has_changed_dir = True
                break 
            elif prev_fast == fast : break

            if fast == slow : return True
        

    return False


def correct_index(i, curr_index, size) :
    if i >= 0 and i < size : return i

    if i >= size : return i % size
    else : 
        index = i + curr_index
        if index >= 0 and index < size : return index
        elif size - ((-1*index) % size) : return size - ((-1*index) % size)
        else : return 0









