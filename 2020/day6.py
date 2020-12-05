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
    return part1, part2

if __name__ == '__main__':
    year, day = os.path.basename(os.getcwd()), re.findall(r'^.*day(\d+).py$', __file__)[0]
    # getInput(year, day) #NOTE: COMMENT ONCE INPUT FETCHED
    lines = [l.strip() for l in open(f'day{day}input.txt').readlines()]
    part1, part2 = main(lines)
    print(part1, part2)
    # submitAnswer(year, day, 1, part1) #NOTE: UNCOMMENT TO AUTO SUBMIT
    # submitAnswer(year, day, 2, part2) #NOTE: UNCOMMENT TO AUTO SUBMIT