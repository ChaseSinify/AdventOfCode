import itertools as iter
import collections as col
import hashlib as hash
import math
import json
import re
import os

from autoInput import getInput, startInputClock
from autoSubmit import submitAnswer

def main(lines):
    # better, more pythonic solution when you see it's just binary :)
    binaries = [int(line.replace("F", "0").replace("B", "1").replace("R", "1").replace("L", "0"), 2) for line in lines]
    part1 = max(binaries)
    sorty = sorted(binaries)
    part2 = next(i + sorty[0] for i in range(len(sorty)) if sorty[i] != i + sorty[0])
    return part1, part2

    #region when you dont notice it's just binary...
    # seats = []
    # highest = 0
    # for line in lines:
    #     low, high = 0, 127
    #     colLow, colHigh = 0, 7
    #     row, col = 0, 0
    #     for c in line:
    #         mid = (high + low) // 2
    #         colMid = (colHigh + colLow) // 2
    #         if c == "F":
    #             high = mid
    #         elif c == "B":
    #             low = mid + 1
    #         elif c == "R":
    #             colLow = colMid + 1
    #         elif c == "L":
    #             colHigh = colMid

    #         if low == high: row = low  
    #         if colLow == colHigh: col = colLow
                         
    #     seatID = row * 8 + col
    #     if seatID > highest:
    #         highest = seatID
    #     seats.append(seatID)

    # ourSeat = None
    # sorty = sorted(seats)
    # for i in range(len(sorty) - 1):
    #     if sorty[i]+1 != sorty[i+1]:
    #         ourSeat = i + sorty[0] + 1
    # return highest, ourSeat
    #endregion
    
if __name__ == '__main__':
    year, day = os.path.basename(os.getcwd()), re.findall(r'^.*day(\d+).py$', __file__)[0]
    # getInput(year, day) #NOTE: COMMENT ONCE INPUT FETCHED
    lines = [l.strip() for l in open(f'day{day}input.txt').readlines()]
    part1, part2 = main(lines)
    print(part1, part2)
    # submitAnswer(year, day, 1, part1) #NOTE: UNCOMMENT TO AUTO SUBMIT
    # submitAnswer(year, day, 2, part2) #NOTE: UNCOMMENT TO AUTO SUBMIT