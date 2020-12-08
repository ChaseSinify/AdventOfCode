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
    return part1, part2

if __name__ == '__main__':
    PART_1 = True # <--- NOTE: Edit submit flag to not autosubmit (for testing)
    year, day = os.path.basename(os.getcwd()), re.findall(r'^.*day(\d+).py$', __file__)[0]
    if not os.path.isfile(f'{os.getcwd()}/day{day}input.txt'):
        getInput(year, day)
    lines = [l.strip() for l in open(f'day{day}input.txt').readlines()]
    part1, part2 = main(lines)
    print(part1, part2)
    SUBMIT = True if input("Submit? (Y: <return> / N: NOT <return>)") == "" else False
    print(SUBMIT)
    if PART_1 and SUBMIT:
        resp = submitAnswer(year, day, 1, part1)
        print(resp)
        if resp == "CORRECT": PART_1 = False
    elif not PART_1 and SUBMIT:
        resp = submitAnswer(year, day, 2, part2)
        if resp == "CORRECT":
            print("Problem complete.")  