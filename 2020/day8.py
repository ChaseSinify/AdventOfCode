import itertools as iter
import collections as col
import hashlib as hash
import math
import json
import re
import os

from autoInput import getInput, startInputClock
from autoSubmit import submitAnswer
"""
Somewhere in the program, either a jmp is supposed to be a nop, 
or a nop is supposed to be a jmp. 
(No acc instructions were harmed in the corruption of this boot code.)
"""
def main(lines):
    # region PART 1
    accum = 0
    seen = set({})
    eip = 0
    op = lines[eip]

    while eip not in seen:
        seen.add(eip) #add this index to seen
        code = op[:3] #get the code
        if code == "nop":
            eip += 1
            op = lines[eip]
        elif code == "acc":
            accum += int(op[4:])
            eip += 1
            op = lines[eip]  
        elif code == "jmp":
            eip = eip+int(op[4:])
            op = lines[eip]
    # #endregion PART 1
    
    #region PART 2
    accum2 = 0
    eip = 0
    target = len(lines) #attempting to execute an instruction immediately after the last instruction in the file.

    # for every line in the file
    for i in range(target):
        temp = list(lines) # get a copy of lines

        # If the current index in the file is not acc, change it and see what happens
        if temp[i][:3] == 'nop':
            temp[i] = 'jmp ' + temp[i][4:]
        elif temp[i][:3] == 'jmp':
            temp[i] = 'nop ' + temp[i][4:]
        else: #dont touch 'acc' operations
            continue
        
        # reset all the helpers
        iterations = 0
        eip = 0
        accum2 = 0

        # while we are not out of bounds and have iterated < 1000 times (because most go on forever)
        while 0 <= eip < target and iterations < 1000:
            iterations += 1 #increment iteration count
            code = temp[eip][:3] #get the code
            if code == "nop":
                eip += 1
            elif code == "acc":
                accum2 += int(temp[eip][4:])
                eip += 1 
            elif code == "jmp":
                eip = eip + int(temp[eip][4:])
        
        # whenever we hit EOF/target, return both parts
        if eip == target:
            return accum, accum2
    #endregion PART 2   


if __name__ == '__main__':
    year, day = os.path.basename(os.getcwd()), re.findall(r'^.*day(\d+).py$', __file__)[0]
    # NOTE: change to check if file exists before calling
    # getInput(year, day) #NOTE: COMMENT ONCE INPUT FETCHED
    lines = [l.strip() for l in open(f'day{day}input.txt').readlines()]
    part1, part2 = main(lines)
    print(part1, part2)
    # submitAnswer(year, day, 1, part1) #NOTE: UNCOMMENT TO AUTO SUBMIT
    # submitAnswer(year, day, 2, part2) #NOTE: UNCOMMENT TO AUTO SUBMIT