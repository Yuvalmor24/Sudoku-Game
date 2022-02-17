'''
Yuval Mor - 14.02.2022

This class has 4 usable functions:

possibleLocation(grid,row,col,num): determines if num can be put on the grid in position (row,col)

uniqueSolution(grid): given a puzzle, the function returns the number of solutions it has

allSolutions(grid): given a puzzle, the function prints all the solutions it has

solve(grid): given a puzzle, the function returns a 2D matrix that repersents the solution of the puzzle
if the given puzzle has more then one solution, the function returns a specific solution.

'''

import copy, random

N = 9

# Given a grid, and an 'index' in the grid
# ret == True iff num can be put in the index, while keeping grid a legal sudoku puzzle
def possibleLocation(grid,row,col,num):
    for i in range (9):
        if ((i != col and grid[row][i] == num) or (i != row and grid[i][col] == num)):
            return False
    
    r = 3 * (row // 3)
    c = 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if ((r+i,c+j) != (row,col) and grid[r+i][c+j] == num):
                return False
    return True


# This function (including the global parm COUNT) is used in order to
# determine the number of possible solutions to a given puzzle
# It is used by the "uniqueSolution" function which is written below
COUNT = 0
def solutionNumber(grid):
    global COUNT
    for i in range(N):
        for j in range(N):
            if (grid[i][j] == 0):
                for num in range(1,10):
                    if possibleLocation(grid,i,j,num):
                        grid[i][j] = num
                        solutionNumber(grid)
                        grid[i][j] = 0
                return
    COUNT += 1

def moreThanOneSolution(grid):
    solNum = [0]
    def rec(grid, solNum):
        for i in range(N):
            for j in range(N):
                if (grid[i][j] == 0):
                    for num in range(1,10):
                        if possibleLocation(grid,i,j,num):
                            grid[i][j] = num
                            rec(grid, solNum)
                            grid[i][j] = 0
                    return
        solNum[0] += 1
        if solNum[0] > 1:
            raise Exception()
    try:
        puzzle = copy.deepcopy(grid)
        rec(puzzle, solNum)
        return False
    except:
        return True

def moreThanThreeSolutions(grid):
    solNum = [0]
    def rec(grid, solNum):
        for i in range(N):
            for j in range(N):
                if (grid[i][j] == 0):
                    for num in range(1,10):
                        if possibleLocation(grid,i,j,num):
                            grid[i][j] = num
                            rec(grid, solNum)
                            grid[i][j] = 0
                    return
        solNum[0] += 1
        if solNum[0] > 3:
            raise Exception()
    try:
        puzzle = copy.deepcopy(grid)
        rec(puzzle, solNum)
        return False
    except:
        return True


# returns a number which represents the number of solutions to the puzzle
# ret == 0 iff no solutions
# ret == 1 iff one solution
# ret == x , x > 1 iff there are x solutions to the puzzle
def uniqueSolution(puzzle):
    global COUNT
    solutionNumber(puzzle)
    temp = COUNT
    COUNT = 0
    return temp


# Prints all possible solutions to a puzzle
def allSolutions(grid):
    for i in range(N):
        for j in range(N):
            if (grid[i][j] == 0):
                for num in range(1,10):
                    if possibleLocation(grid,i,j,num):
                        grid[i][j] = num
                        allSolutions(grid)
                        grid[i][j] = 0
                return
    print("Solution: ")
    for line in grid: print(line)


# Returns the solution to a puzzle (or 1 of the solutions, if there are more then 1 solutions)
def solve(puzzle):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                for num in range(1,10):
                    if possibleLocation(puzzle, i, j, num):
                        puzzle[i][j] = num
                        if not solve(puzzle):
                            puzzle[i][j] = 0
                        else:
                            return puzzle
                return None
    print("Solved!")
    return puzzle



# sod =  [[2, 0, 1, 0, 9, 0, 0, 0, 3],
#         [0, 0, 0, 0, 0, 0, 8, 9, 0],
#         [0, 0, 8, 0, 5, 0, 6, 0, 7],
#         [0, 0, 5, 0, 0, 0, 1, 6, 0],
#         [0, 1, 0, 0, 8, 7, 0, 4, 2],
#         [0, 0, 0, 1, 6, 9, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 8],
#         [0, 0, 0, 2, 0, 0, 5, 0, 0],
#         [5, 4, 3, 0, 1, 8, 0, 0, 0]]

# print("Output of moreThanThreeSolutions: " + str(moreThanOneSolution(sod)))

# sod =  [[0, 3, 0, 0, 0, 0, 0, 0, 0],
#         [5, 0, 1, 0, 0, 0, 0, 0, 0],
#         [0, 0, 6, 9, 7, 0, 0, 2, 0],
#         [0, 0, 0, 0, 1, 0, 0, 0, 0],
#         [0, 0, 8, 0, 0, 5, 0, 0, 0],
#         [0, 4, 0, 0, 0, 0, 3, 0, 9],
#         [0, 9, 7, 0, 0, 0, 0, 0, 0],
#         [2, 0, 0, 0, 8, 0, 5, 1, 0],
#         [0, 0, 0, 0, 0, 0, 0, 0, 8]]
# for row in solve(sod): print(row)
# print("Number of Solutions is: " + str(uniqueSolution(sod)))
# clues = 0
# for i in range(9):
#     for j in range(9):
#         if (sod[i][j] != 0):
#             clues += 1
# print(clues)