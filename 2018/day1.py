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
    # PART 1 
    part1, part2 = 0, 0
    for line in lines:
        part1 += int(line)

    # PART 2
    f = set({})
    i = 0
    while True:
        part2 += int(lines[i % len(lines)])
        if part2 in f:
            break
        f.add(part2)
        i += 1

    return part1, part2

if __name__ == '__main__':
    year, day = os.path.basename(os.getcwd()), re.findall(r'^.*day(\d+).py$', __file__)[0]
    # NOTE: change to check if file exists before calling
    # getInput(year, day) #NOTE: COMMENT ONCE INPUT FETCHED
    lines = [l.strip() for l in open(f'day{day}input.txt').readlines()]
    part1, part2 = main(lines)
    print(part1, part2)
    # submitAnswer(year, day, 1, part1) #NOTE: UNCOMMENT TO AUTO SUBMIT
    # submitAnswer(year, day, 2, part2) #NOTE: UNCOMMENT TO AUTO SUBMIT