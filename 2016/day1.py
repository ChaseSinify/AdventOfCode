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

    # PART 1 & PART 2
    S = set({})
    flag = True
    lines = lines[0].split(", ")
    part1, part2 = 0, 0
    x,y = 0,0
    directions = ['N', 'E', 'S', 'W']
    dir = 0
    lastX, lastY = 0, 0
    for item in lines:
        turn, distance = item[0], int(item[1:])
        if turn == "R": dir = (dir + 1) % 4
        elif turn == "L": dir = (dir - 1) % 4

        if directions[dir] == "N":
            y += distance
            lastY = y
        elif directions[dir] == "E":
            x += distance
            lastX = x
        elif directions[dir] == "S":
            y -= distance
            lastY = y
        elif directions[dir] == "W":
            x -= distance
            lastX = x
        if x == lastX: # x didnt change, add new y points to set, update last y
            tempy, templast = y, lastY
            if y < lastY: tempy, templast = lastY, y
            for yi in range(tempy, templast):
                if (x, yi) in S:
                    return 0, abs(x) + abs(yi)
                S.add((x, yi))
            lastY = y
        elif y == lastY: # y didnt change, add new x points to set, update last x
            tempx, templast = x, lastX
            if y < lastY: tempy, templast = lastY, y
            for xi in range(tempx, templast):
                if (xi, y) in S:
                    return 0, abs(xi) + abs(y)
                S.add((xi, y))
            lastY = y
    part1 = abs(x) + abs(y)

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