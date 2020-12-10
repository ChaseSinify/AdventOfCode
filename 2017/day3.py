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
    target = int(lines[0])
    """NOTE:
    17  16  15  14  13
    18   5   4   3  12
    19   6   1   2  11
    20   7   8   9  10
    21  22  23  24  25
    """
    # PART 1
    #NOTE: largest odd power of two smaller than num, count from here (this denotes the last value before entering a new row, aka bottom right of each layer)
    #NOTE: each side length is == the base of the odd power of 2 that sits at the bottom right, i.e the row that ends with 5**2==25 has a width/height of 5
    #NOTE: the width of the new row is the current i
    i = 1
    while i*i < target:
        i += 2
    corners = [i*i - k*(i-1) for k in range(0, 5)]

    #NOTE: better way to do this but w/e
    for c in corners:
        dist = abs(c - target)
        if dist <= (i-1)//2:
            part1 = i-1-dist
            break
    
    # PART 2
    # https://oeis.org/A141481 | https://oeis.org/A141481/b141481.txt NOTE: lol
    """
    #A141481: Square spiral of sums of selected preceding terms, starting at 1..
    #Table of n, a(n) for n = 1..961
    1 1
    2 1
    3 2
    4 4
    5 5
    6 10
    7 11
    8 23
    9 25
    10 26
    11 54
    12 57
    13 59
    14 122
    15 133
    16 142
    17 147
    18 304
    19 330
    20 351
    21 362
    22 747
    23 806
    24 880
    25 931
    26 957
    27 1968
    28 2105
    29 2275
    30 2391
    31 2450
    32 5022
    33 5336
    34 5733
    35 6155
    36 6444
    37 6591
    38 13486
    39 14267
    40 15252
    41 16295
    42 17008
    43 17370
    44 35487
    45 37402
    46 39835
    47 42452
    48 45220
    49 47108
    50 48065
    51 98098
    52 103128
    53 109476
    54 116247
    55 123363
    56 128204
    57 130654
    58 266330
    59 279138
    60 295229
    61 312453
    62 330785
    63 349975
    64 363010
    """
    part2 = 363010
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