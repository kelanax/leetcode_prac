'''

PROBLEM: 

Design a custom stack, Min Stack. Implement the Min Number(), Push() and Pop() methods: 

- Pop(): Removes and returns from the stack the value that was most recently pushed on to it. 
- Push(): Pushes the provided value on to the stack. 
- Min Number(): Returns the minimum value in the stack in O(1) time.

--------------------------------
PATTERN: CUSTOM DATA STRUCTURES
--------------------------------

'''




from stack import MainStack


class MinStack:
    # Initialize min and main stack here
    def __init__(self):

        self.main_stack = []
        self.min_stack = []
        
        

    # Remove and returns value from the stack
    def pop(self):

        if self.main_stack and self.min_stack :
            self.min_stack.pop()
            val = self.main_stack.pop() 
            return val
        
        return None

    # Pushes values into the stack
    def push(self, value):

        if self.main_stack and self.min_stack :

            self.main_stack.append(value)
            min_so_far = self.min_stack[-1]
            if value < min_so_far : self.min_stack.append(value)
            else : self.min_stack.append(min_so_far)
        else :
            self.main_stack.append(value)
            self.min_stack.append(value)

    # Returns minimum value from stack
    def min_number(self):

        if self.min_stack : 
            val = self.min_stack[-1]
            return val

        return None

















        






