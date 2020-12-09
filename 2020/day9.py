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

def main(lines):
    # print(lines)
    part1, part2 = 0, 0

    """
    NOTE:
    """
    # PART 1
    lines = [int(x) for x in lines]
    for i in range(25, len(lines)):

        # reset sums
        sums = set({})

        # generate all the sums of the last 25
        for x in range(i-25, i):
            for y in range(i-25, i):
                if x != y:
                    sums.add(lines[x] + lines[y])

        if lines[i] not in sums:
            part1 = lines[i]
            break
    
    # PART 2 -- Didn't even attempt to optimze it
    end = 0
    for i in range(len(lines)-1):
        end = i + 1
        while end < len(lines):
            if sum(lines[i:end+1]) == part1:
                part2 = min(lines[i:end+1]) + max(lines[i:end+1])
                return part1, part2
            end += 1
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