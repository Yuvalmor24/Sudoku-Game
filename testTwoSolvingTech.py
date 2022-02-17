''' This class purpose is to test the time complexity it takes the computer
    to solve a puzzle, with two different algorithms.
    both of the algorithm are very much alike the 'solve' algorithm in the sudokuSolver class,
    but they both differ on one line exactly (lines 38, 52 of the code).
    Both implement a backtracking recursive algorithm used in order to solve to puzzle.

    The first one (solvingTechniqueOne) tries to put in every empty cell in the grid a number,
    in a linear order from 1-9 ('linear trial and error').
    The second one (solvingTechniqueTwo) tries to put in every empty cell in the grid anumber,
    in a random order of the number 1-9 ('random trial and error'), without allowing any number
    to repeat itself more then once.

    The first test is checking the difference in the time it takes the two methods to solve a given set
    of puzzles in a specific difficulty (of size and difficulty which is decided by the user)
    
    As you can see (run) The results of the first test shows clearly that the random algorihtm is slower.
    
    One reason for this may be the numerous amount of calls of the random.sample function, done by the
    second algorithm (random). Therefore, in order to check the effect of the time it takes to perform the
    random.sample function, I created the Second Test.

    The second test does exactly the same thing as the first, although it slightly changes the first algorithm
    in such a way that it will also call the random.sample function exactly the amount of times the second one
    calls it. 

    You are invited to run the second test, and watch the results yourself. 
    '''


import time, random, sudokuSolver, puzzleGen

countSolvedOne = 0
def solvingTechniqueOne(puzzle):
    global countSolvedOne
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                for num in range(1,10):
                    if sudokuSolver.possibleLocation(puzzle, i, j, num):
                        puzzle[i][j] = num
                        solvingTechniqueOne(puzzle)
                        puzzle[i][j] = 0
                return
    countSolvedOne += 1

countSolvedTwo = 0
def solvingTechniqueTwo(puzzle):
    global countSolvedTwo
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                for num in random.sample(range(1,10),9):
                    if sudokuSolver.possibleLocation(puzzle, i, j, num):
                        puzzle[i][j] = num
                        solvingTechniqueTwo(puzzle)
                        puzzle[i][j] = 0
                return
    countSolvedTwo += 1

def solvingTechniqueOneNormalized(puzzle):
    global countSolvedOne
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                random.sample(range(1,10),9)
                for num in range(1,10):
                    if sudokuSolver.possibleLocation(puzzle, i, j, num):
                        puzzle[i][j] = num
                        solvingTechniqueOneNormalized(puzzle)
                        puzzle[i][j] = 0
                return
    countSolvedOne += 1


def testTwoSolvingTechniques(num, difficulty, numOfTest):
    puzzles = [puzzleGen.PuzzleGen(difficulty)[0] for i in range (num)]
    if numOfTest == 1:
        before = time.time()
        for puzzle in puzzles:
            solvingTechniqueOne(puzzle)
        after = time.time()
        timeOne = after - before
        print("Technique one (not random) solved the " + str(countSolvedOne) + " in time: " + str(timeOne) + " seconds." )
        print("Average time for solution: " + str((timeOne/num) * 1000) + " ms")
        print ("---------------------------------------------")
        before = time.time()
        for puzzle in puzzles:
            solvingTechniqueTwo(puzzle)
        after = time.time()
        timeOne = after - before
        print("Technique two (random) solved the " + str(countSolvedTwo) + " in time: " + str(timeOne) + " seconds." )
        print("Average time for solution: " + str((timeOne/num) * 1000) + " ms")
    elif numOfTest == 2:
        before = time.time()
        for puzzle in puzzles:
            solvingTechniqueOneNormalized(puzzle)
        after = time.time()
        timeOne = after - before
        print("Technique one (not random, normalized) solved the " + str(countSolvedOne) + " in time: " + str(timeOne) + " seconds." )
        print("Average time for solution: " + str((timeOne/num) * 1000) + " ms")
        print ("---------------------------------------------")
        before = time.time()
        for puzzle in puzzles:
            solvingTechniqueTwo(puzzle)
        after = time.time()
        timeOne = after - before
        print("Technique two (random) solved the " + str(countSolvedTwo) + " in time: " + str(timeOne) + " seconds." )
        print("Average time for solution: " + str((timeOne/num) * 1000) + " ms")



numberOfTrials = input("Please enter number of puzzles you want to test with:\n")
print ("---------------------------------------------")
difficulty = input("Please enter the difficulty of the puzzles (1 = easy, 2 = medium, 3 = hard)." + '\n' +
                    "Note that the higher the difficulty is, the longer it takes to generate the puzzle and solve it:\n")

print ("---------------------------------------------")

numOfTest = input("Please enter the number of test (1 for the first test, 2 for the second test):\n")
print ("---------------------------------------------")

testTwoSolvingTechniques(int(numberOfTrials), int(difficulty), int(numOfTest))