'''

PROBLEM: 

In a single-player jump game, the player starts at one end of a series of squares, with the 
goal of reaching the last square. 

At each turn, the player can take up to s steps towards the last square, where s is the value of the current square. For example, if the value of 
the current square.

For example, if the value of the current square is 3 , the player can take either 3 steps, or 
2 steps, or 1 step in the direction of the last square. The player cannot move in the opposite 
direction, that is, away from the last square. 

You've been provided with the nums integer array, representing the series of squares. 

You're initially positioned at the first index of the array. Find the minimum number of 
jumps needed to reach the last index of the array. You may assume that you can always 
reach the last index.

---------------------------
PATTERN: GREEDY TECHNIQUES
---------------------------

'''


def jump_game_two(nums):
    
    farthest_jump = current_jump = num_jumps = 0

    for i in range(len(nums)) : 

        if current_jump >= (len(nums) - 1) : return num_jumps

        farthest_jump = max(farthest_jump, i + nums[i])

        if i == current_jump :
            
            num_jumps += 1
            current_jump = farthest_jump

            


    return num_jumps


