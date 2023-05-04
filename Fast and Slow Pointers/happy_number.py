'''
PROBLEM: 

Write an algorithm to determine if a number, n, is happy.

A happy number is a number defined by the following process:

- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it loops endlessly 
  in a cycle which does not include 1
- Those numbers for which this process ends in 1 are happy.
Return TRUE if n is a happy number, and FALSE if not.

--------------------------------
PATTERN: FAST AND SLOW POINTER  
--------------------------------

'''


def is_happy_number(n):
    #Write your code here

    slow = n
    fast = sum_of_squared_digits(n)

    while True :

        if fast == 1 : return True

        if slow == fast : return False

        slow = sum_of_squared_digits(slow)
        fast = sum_of_squared_digits(sum_of_squared_digits(fast))




def sum_of_squared_digits(number): # Helper function that calculates the sum of squared digits.
    total_sum = 0
    while number > 0:
        digit = number % 10
        number = number // 10
        total_sum += digit ** 2
    return total_sum


