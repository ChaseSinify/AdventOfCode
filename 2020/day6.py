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
    print(lines)
    part1, part2 = 0, 0
    yes = {}
    rows = 0
    count = 0
    for line in lines:
        if line == "":
            for k,v in yes.items():
                if v == rows:
                    count += 1
            #new item
            part2 += count
            count = 0
            rows = 0
            yes.clear()
        else:
            rows += 1
            for char in line:
                if char not in yes:
                    yes[char] = 1
                else:
                    yes[char] += 1

    for k,v in yes.items():
        if v == rows:
            count += 1
    part2 += count
    return part1, part2

if __name__ == '__main__':
    year, day = os.path.basename(os.getcwd()), re.findall(r'^.*day(\d+).py$', __file__)[0]
    # getInput(year, day) #NOTE: COMMENT ONCE INPUT FETCHED
    lines = [l.strip() for l in open(f'day{day}input.txt').readlines()]
    part1, part2 = main(lines)
    print(part1, part2)
    # submitAnswer(year, day, 1, part1) #NOTE: UNCOMMENT TO AUTO SUBMIT
    # submitAnswer(year, day, 2, part2) #NOTE: UNCOMMENT TO AUTO SUBMIT