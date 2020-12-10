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
    # PART 1
    part1, part2 = 0, 0
    nums = sorted([int(x) for x in lines])
    nums = [0] + nums + [nums[-1] + 3] #NOTE: added this to make the logic easier for both parts, since we start at 0 and our device is always max value + 3

    ones, threes = 0, 0
    for i in range(1, len(nums)):
        if abs(nums[i-1] - nums[i]) == 3: threes += 1
        elif abs(nums[i-1] - nums[i]) == 1: ones += 1

    part1 = ones * threes

    # PART 2
    """
    #NOTE: 0, 1, 2, 3, 4, 5, 6, 7, 8, 11
    The key is the value from the nums array, the value is the sum of all of the nodes that can touch it
    i.e. in the above series, 3 can be reached from 0, 1, or 2. Therefore, we add (mappy[0] + mappy[1] + mappy[2]) -> mappy[3]'s value
    """
    #NOTE:hard coded the first 3 just so its easier to think about our loop without the additional edge case
    mappy = {0: 1, 1: 1, 2: 2} 
    
    # start at 3 (since we hard coded the first 3), always check three behind, if they are in range (aka 3 away or less), add mappy[their value] to the sum for this position
    for i in range(3, len(nums)):
        mappy[nums[i]] = 0

        # check the last three values in the sorted nums array from this position
        for x in range(i-3, i):

            # if the current value at this position in nums - the previous value is within the range of three, add the value of the sum position in the map to the temp sum
            if nums[i] - nums[x] <= 3:
                mappy[nums[i]] += mappy[nums[x]]

    part2 = max(mappy.values())
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