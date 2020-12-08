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

    # PART 1
    twos = 0
    threes = 0
    two = False
    three = False
    for line in lines:
        counts = col.Counter(line)
        for c in counts:
            if counts[c] == 2 and not two:
                twos += 1
                two = True
            if counts[c] == 3 and not three:
                threes += 1
                three = True
        two = False
        three = False
    part1 = twos * threes

    # PART 2
    index = 0 #the index of the diff char
    for x in lines:
        for y in lines:
            one = False # track if we have a diff char
            for i in range(len(x)):
                if x[i] != y[i]: # diff char
                    index = i # mark the index of the diff char
                    if one: # if we've already seen a diff char with this pair, break
                        index = 0 # reset index of diff char
                        one = False # reset before break so we can see if it passed all
                        break
                    one = True # mark as diff seen

            # if this is true, we only had 1 diff char and didnt break
            if one:
                part2 = x[:index] + x[index+1:]
                return part1, part2 # return both parts

if __name__ == '__main__':
    year, day = os.path.basename(os.getcwd()), re.findall(r'^.*day(\d+).py$', __file__)[0]
    # NOTE: change to check if file exists before calling
    # getInput(year, day) #NOTE: COMMENT ONCE INPUT FETCHED
    lines = [l.strip() for l in open(f'day{day}input.txt').readlines()]
    part1, part2 = main(lines)
    print(part1, part2)
    # submitAnswer(year, day, 1, part1) #NOTE: UNCOMMENT TO AUTO SUBMIT
    # submitAnswer(year, day, 2, part2) #NOTE: UNCOMMENT TO AUTO SUBMIT