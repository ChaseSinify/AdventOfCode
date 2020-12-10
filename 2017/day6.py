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
    nums = [int(x) for x in lines[0].split()]
    
    seen = set({})
    seen.add(nums.__repr__()) # add the base repr
    cycles = 0

    cycleStart = ""

    # PART 1
    while True:
        cycles += 1
        count = max(nums) 
        index = (nums.index(count) + 1) % len(nums) #NOTE: Starting with the next bank

        # NOTE: don't forget to set the current max location to 0 :)
        nums[nums.index(count)] = 0

        while count > 0:
            nums[index] += 1
            index = (index + 1) % len(nums)
            count -= 1
        
        # exit condition
        if nums.__repr__() in seen:
            part1 = cycles
            cycleStart = nums.__repr__()
            break
            
        # add this repr to the set of seen
        seen.add(nums.__repr__())

    # PART 2
    cycles = 0

    while True:
        cycles += 1
        count = max(nums) 
        index = (nums.index(count) + 1) % len(nums) #NOTE: Starting with the next bank

        # NOTE: don't forget to set the current max location to 0 :)
        nums[nums.index(count)] = 0

        while count > 0:
            nums[index] += 1
            index = (index + 1) % len(nums)
            count -= 1
        
        # exit condition
        if nums.__repr__() == cycleStart:
            part2 = cycles
            break

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