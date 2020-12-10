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
    # print(lines)
    part1, part2 = 0, 0
    jmps = [int(x) for x in lines]
    jmps2 = [int(x) for x in lines]

    # PART 1
    ecx = 0
    eip = 0
    while True:
        try:
            jmps[eip] += 1
            eip += jmps[eip] - 1
            ecx += 1
        except:
            break
    part1 = ecx

    # PART 2 NOTE: dont reuse the same tampered input for part 2 :)
    ecx = 0
    eip = 0
    while eip >= 0 and eip < len(jmps2):
        if jmps2[eip] >= 3:
            jmps2[eip] -= 1
            eip = eip + jmps2[eip] + 1
        else:
            jmps2[eip] += 1
            eip = eip + jmps2[eip] - 1
        ecx += 1
    part2 = ecx

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