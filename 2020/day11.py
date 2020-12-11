import itertools as iter
import collections as col
import hashlib as hash
import math
import json
import re
import os
import sys

from autoInput import getInput, startInputClock
from autoSubmit import submitAnswer

def main(grid):
    part1, part2 = 0, 0
    
    #NOTE: padding the array to make bounds easy --> cheese
    grid = ["X" * 99] + grid + ["X" * 99]
    for i in range(len(grid)):
        grid[i] = "X" + grid[i]  + "X"

    grid2 = grid.copy()
    
    rLen, cLen = len(grid[0]), len(grid) #row length and col length

    toChange = {} #NOTE: this holds all the points we need to update after a loop

    """
    #NOTE: since we padded the file, we always check 1 in
    """
    #region PART 1
    while True: #NOTE: We loop as long as the "game of life" has created some change
        
        # for all of the coordinates
        for rc in iter.product(range(1, cLen-1), range(1, rLen-1)):
            #NOTE: if any of the rules apply, update this cell <key>
            #NOTE: and what it should change to <value> in the toChange map

            #set row and col for easy thinking
            row, col = rc[0], rc[1]
            seat = grid[row][col]

            if seat == ".": continue #we don't touch the floors (.)

            occupied = 0 #NOTE: (#)
            
            #NOTE: check the 8 squares
            #Check top left: (-1, -1)
            if grid[row-1][col-1] == "#": occupied += 1

            #Check top: (-1, 0)
            if grid[row-1][col] == "#": occupied += 1

            #Check top right: (-1, 1)
            if grid[row-1][col+1] == "#": occupied += 1

            #Check right: (0, 1)
            if grid[row][col+1] == "#": occupied += 1

            #Check bottom right: (1, 1)
            if grid[row+1][col+1] == "#": occupied += 1

            #Check bottom: (1, 0)
            if grid[row+1][col] == "#": occupied += 1

            #Check bottom left: (1, -1)
            if grid[row+1][col-1] == "#": occupied += 1

            #Check left: (0, -1)
            if grid[row][col-1] == "#": occupied += 1

            """
            #NOTE: Rules:
            If a seat is empty (L) and there are no occupied seats adjacent to it, 
                the seat becomes occupied.
            If a seat is occupied (#) and four or more seats adjacent to it are also occupied, 
                the seat becomes empty.
            Otherwise, 
                the seat's state does not change.
            """
            if seat == "L" and not occupied:
                toChange[(row, col)] = "#"
            elif seat == "#" and occupied >= 4:
                toChange[(row, col)] = "L"
            
        #if no cells need changing, we are done, count seats (#) and exit
        if not toChange:
            for rc in iter.product(range(1, cLen-1), range(1, rLen-1)):
                row, col = rc[0], rc[1]
                if grid[row][col] == "#":
                    part1 += 1
            break
        else:
            pass #NOTE: update the changes
            for k,v in toChange.items():
                row, col = k[0], k[1]
                grid[row] = grid[row][:col] + v + grid[row][col+1:]
            toChange = {} #reset the changes map
    # endregion PART 1

    #region PART 2:
    while True: #NOTE: We loop as long as the "game of life" has created some change
        
        # for all of the coordinates
        for rc in iter.product(range(1, cLen-1), range(1, rLen-1)):
            #set row and col for easy thinking
            row, col = rc[0], rc[1]
            seat = grid2[row][col]

            if seat == ".": continue #we don't touch the floors (.)

            occupied = 0 #NOTE: (#)
            

            """
            #NOTE: Seeing an L counts as a break condition, we can't see through them
            The leftmost empty seat below would only see one empty seat, 
            but cannot see any of the occupied ones:
            .............
            .L.L.#.#.#.#.
            .............
            """
            #NOTE: check the 8 directions until seat found or border(X) hit
            #Check top left: (-1, -1)
            tempRow, tempCol = row-1, col-1
            while True:
                if grid2[tempRow][tempCol] == "#": 
                    occupied += 1
                    break
                elif grid2[tempRow][tempCol] == "L":
                    break
                elif grid2[tempRow][tempCol] == "X":
                    break
                tempRow -= 1
                tempCol -= 1

            #Check top: (-1, 0)
            tempRow, tempCol = row-1, col
            while True:
                if grid2[tempRow][tempCol] == "#": 
                    occupied += 1
                    break
                elif grid2[tempRow][tempCol] == "L":
                    break
                elif grid2[tempRow][tempCol] == "X":
                    break
                tempRow -= 1

            #Check top right: (-1, 1)
            tempRow, tempCol = row-1, col+1
            while True:
                if grid2[tempRow][tempCol] == "#": 
                    occupied += 1
                    break
                elif grid2[tempRow][tempCol] == "L":
                    break
                elif grid2[tempRow][tempCol] == "X":
                    break
                tempRow -= 1
                tempCol += 1

            #Check right: (0, 1)
            tempRow, tempCol = row, col+1
            while True:
                if grid2[tempRow][tempCol] == "#": 
                    occupied += 1
                    break
                elif grid2[tempRow][tempCol] == "L":
                    break
                elif grid2[tempRow][tempCol] == "X":
                    break
                tempCol += 1

            #Check bottom right: (1, 1)
            tempRow, tempCol = row+1, col+1
            while True:
                if grid2[tempRow][tempCol] == "#": 
                    occupied += 1
                    break
                elif grid2[tempRow][tempCol] == "L":
                    break
                elif grid2[tempRow][tempCol] == "X":
                    break
                tempRow += 1
                tempCol += 1

            #Check bottom: (1, 0)
            tempRow, tempCol = row+1, col
            while True:
                if grid2[tempRow][tempCol] == "#": 
                    occupied += 1
                    break
                elif grid2[tempRow][tempCol] == "L":
                    break
                elif grid2[tempRow][tempCol] == "X":
                    break
                tempRow += 1

            #Check bottom left: (1, -1)
            tempRow, tempCol = row+1, col-1
            while True:
                if grid2[tempRow][tempCol] == "#": 
                    occupied += 1
                    break
                elif grid2[tempRow][tempCol] == "L":
                    break
                elif grid2[tempRow][tempCol] == "X":
                    break
                tempRow += 1
                tempCol -= 1

            #Check left: (0, -1)
            tempRow, tempCol = row, col-1
            while True:
                if grid2[tempRow][tempCol] == "#": 
                    occupied += 1
                    break
                elif grid2[tempRow][tempCol] == "L":
                    break
                elif grid2[tempRow][tempCol] == "X":
                    break
                tempCol -= 1

            """
            #NOTE: Rules:
            If a seat is empty (L) and there are no occupied seats adjacent to it, 
                the seat becomes occupied.
            If a seat is occupied (#) and FIVE or more seats adjacent to it are also occupied, 
                the seat becomes empty.
            Otherwise, 
                the seat's state does not change.
            """
            if seat == "L" and not occupied:
                toChange[(row, col)] = "#"
            elif seat == "#" and occupied >= 5:
                toChange[(row, col)] = "L"
            
        #if no cells need changing, we are done, count seats (#) and exit
        if not toChange:
            for rc in iter.product(range(1, cLen-1), range(1, rLen-1)):
                row, col = rc[0], rc[1]
                if grid2[row][col] == "#":
                    part2 += 1
            break
        else:
            for k,v in toChange.items():
                row, col = k[0], k[1]
                grid2[row] = grid2[row][:col] + v + grid2[row][col+1:]
            toChange = {} #reset the changes map
    #endregion PART 2

    return part1, part2

if __name__ == '__main__':
    PART_1 = False # NOTE: FLIP FOR PART 2 SUBMISSIONS

    year, day = os.path.basename(os.getcwd()), re.findall(r'^.*day(\d+).py$', __file__)[0]
    if not os.path.isfile(f'{os.getcwd()}/day{day}input.txt'):
        getInput(year, day)

    lines = [l.strip() for l in open(f'day{day}input.txt').readlines()]

    part1, part2 = main(lines)
    print(part1, part2)

    SUBMIT = True if input("Submit? (Y: <return> / N: NOT <return>)") == "" else False
    if PART_1 and SUBMIT:
        resp = submitAnswer(year, day, 1, part1)
        print(resp)
        if resp == "CORRECT": PART_1 = False # NOTE: This is where we update the db file
    elif not PART_1 and SUBMIT:
        resp = submitAnswer(year, day, 2, part2)
        print(resp)
        if resp == "CORRECT": print("Problem complete.") # NOTE: This is where we update the db file