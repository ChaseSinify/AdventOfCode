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
    # print(lines)
    part1, part2 = 0, 0

    """
    NOTE:   just track every point we see into set <A>
            if we ever encounter a new point that is in <A>,
            add it to set <B>
            Part 1 == len(<B>),
            a.k.a all the points we say more than once
    """
    # PART 1
    a = set({}) # points seen once
    b = set({}) # ponts seen more than once
    for line in lines:
        id, locX, locY, sizeX, sizeY = map(int, re.findall(r'^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$', line)[0])
        for x in iter.product([x for x in range(locX, locX + sizeX)], [y for y in range(locY, locY + sizeY)]): a.add(x) if x not in a else b.add(x)
    
    # PART 2
    for line in lines:
        disjoint = True
        id, locX, locY, sizeX, sizeY = map(int, re.findall(r'^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$', line)[0])
        for x in iter.product([x for x in range(locX, locX + sizeX)], [y for y in range(locY, locY + sizeY)]):
            if x in b:
                disjoint = False
                break
        if disjoint:
            part2 = id
            break
    return len(b), part2

if __name__ == '__main__':
    year, day = os.path.basename(os.getcwd()), re.findall(r'^.*day(\d+).py$', __file__)[0]
    # NOTE: change to check if file exists before calling
    # getInput(year, day) #NOTE: COMMENT ONCE INPUT FETCHED
    lines = [l.strip() for l in open(f'day{day}input.txt').readlines()]
    part1, part2 = main(lines)
    print(part1, part2)
    # submitAnswer(year, day, 1, part1) #NOTE: UNCOMMENT TO AUTO SUBMIT
    # submitAnswer(year, day, 2, part2) #NOTE: UNCOMMENT TO AUTO SUBMIT