'''

PROBLEM: 



---------------------------
PATTERN: GREEDY TECHNIQUES
---------------------------

'''





def jump_game(nums):
    target = len(nums) - 1
    if target <= 1 : return True


    for i in range(nums[0], 0, -1) :
        j = i

        while True :

            if j >= target : return True

            if nums[j] == 0 and j < target : break
            elif nums[j] == 0 : return False
            else : j = j + nums[j]

    return False
