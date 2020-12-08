from enum import Flag
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
    print(lines)
    part1, part2 = 0, 0
    # PART 1
    part1 = sum(max([int(x) for x in line.split('\t')]) - min([int(x) for x in line.split('\t')]) for line in lines)

    # PART 2
    for line in lines:
        for x in line.split():
            for y in line.split():
                print(x, y)
                if int(x) > int(y):
                    if int(x) % int(y) == 0:
                        part2 += int(x) // int(y)
                        break 
                    
    return part1, part2

if __name__ == '__main__':
    PART_1 = False

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
        if resp == "CORRECT": PART_1 = False
    elif not PART_1 and SUBMIT:
        resp = submitAnswer(year, day, 2, part2)
        print(resp)
        if resp == "CORRECT": print("Problem complete.")  