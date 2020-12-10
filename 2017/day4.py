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

    # PART 1
    valid = 0
    for line in lines:
        S = set({})
        for word in line.split():
            if word in S:
                break
            S.add(word)
        if len(S) == len(line.split()):
            valid += 1
        S = set({})
    part1 = valid

    
    # PART 2 NOTE: Lexicographically sorted words remove any need to compare permutations, probs even faster way but this works good enough
    valid = 0
    S = set({})
    for line in lines:
        for word in line.split():
            word = ''.join(sorted(word))
            if word in S:
                break
            S.add(word)
        if len(S) == len(line.split()):
            valid += 1
        S = set({})
    part2 = valid

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