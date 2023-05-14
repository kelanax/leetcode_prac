'''

PROBLEM: 

Given a chessboard of size nxn , determine how many ways n queens can be placed on the board, 
such that no two queens attack each other. 

A queen can move horizontally, vertically, and diagonally on a chessboard. One queen can be 
attacked by another queen if both share the same row, column, or diagonal.

-----------------------
PATTERN: BACKTRACKING
-----------------------

'''





from backtracking import *


# Tip: You may use some of the code templates provided
# in the support files


def solve_n_queens(n):
  
  board = [[0] * n for i in range(n)]
  
  solutions = helper(board, 0, n)

  return solutions


def valid_column(board, col, n) :
  for row in range(n) :
    if board[row][col] == 1 : return False
  return True



def valid_diagonal(board, i, j, n) :
  row, col = i + 1, j + 1
  while row < n and col < n :
    if board[row][col] == 1 : return False
    row += 1
    col += 1

  row, col = i - 1, j - 1 
  while row >= 0 and col >= 0 : 
    if board[row][col] == 1 : return False
    row -= 1
    col -= 1

  row, col = i - 1, j + 1
  while row >= 0 and col < n:
    if board[row][col] == 1:
        return False
    row -= 1
    col += 1

  row, col = i + 1, j - 1
  while row < n and col >= 0:
    if board[row][col] == 1:
        return False
    row += 1
    col -= 1
  return True



def valid_row(board, row, n) :
  for col in range(n) :
    if board[row][col] == 1 : return False
  return True

def helper(board, row , n) :

  if row >= n : return 1
  solutions = 0

  for col in range(n) : 

    if (valid_column(board, col, n)) and\
    (valid_diagonal(board, row, col, n)) and\
    (valid_row(board, row, n)) :

       board[row][col] = 1 

       solutions += helper(board, row + 1 , n)

       board[row][col] = 0

  return solutions


    



  









