import itertools as iter
import collections as col
import hashlib as hash
import math
import json
import re
import os

from autoInput import getInput, startInputClock
from autoSubmit import submitAnswer

#TODO: Refactor this and problem 6 to not be garbage

"""How many bag colors can eventually contain at least one shiny gold bag?"""
def main(lines):
    #testing
    shinyBags = set({}) #stores the bags that can 'eventually hold shiny bags'
    bagsMap = {}

    # build up the dict of all the bags
    for line in lines:
        bagItems = {} #bag type : count"
        splitContain = line.split("contain ")
        keyBag = splitContain[0].replace("bags", "").strip()
        keyBagContents = splitContain[1].split(", ")
        for bag in keyBagContents:
            if bag == "no other bags.":
                # print(bag)
                break
            bagItems[bag[2:].replace("bags", "").replace("bag", "").replace(".", "").strip()] = bag[0] # print(f'{bag[2:].replace("bags", "").replace("bag", "").replace(".", "").strip()}: {bag[0]}')
            
        bagsMap[keyBag] = bagItems

    #region PART 1 NOTE: BRAINDEAD METHOD ----------------------------------------------------------------------------------------------------------------------------
    bagsMap2 = bagsMap.copy() # hacky

    shinyBags.add("shiny gold") # start by adding the shiny gold bag to the map #NOTE important -> THIS BAG DOES NOT COUNT
    addedBag = True # tracks if we added a new bag (aka a new path length) to the shinyBags set on a given loop, if we DID NOT, we are done (see notes)
    toDelete = [] # items we need to delete after a given loop

    while addedBag:
        addedBag = False #start with false, update to true if we ever add a bag
        for k,v in bagsMap.items(): # for every bag still in the bagsMap (we remove ones that are confirmed to have a path to shiny as we loop)
            for i in v: # for each bag this bag leads to
                if i in shinyBags: # if this value is in the set of bags that lead to a shiny
                    shinyBags.add(k) # add this key to the set of shinyBags, which holds any bag that is confirmed to have a path to a shiny
                    toDelete.append(k) # add this item to list of those to be deleted
                    addedBag = True # if we added a bag, flip this and keep looping

        # delete the ones we touched this pass
        for item in toDelete:
            if item in bagsMap:
                bagsMap.pop(item)
        
        toDelete = [] # reset
    #endregion BRAINDEAD METHOD -------------------------------------------------------------------------------------------------------------------------------

    #region PART 2
    shinyGold = bagsMap2["shiny gold"] # grab the shiny bag
    totalBags = 0 # the total count of bags starting from our shiny gold bag
    q = col.deque() # get a new queue

    # init the queue with the first level of bags directly from our shiny bag
    for bag, count in shinyGold.items():
        for i in range(int(count)): # add count bags to the queue
            q.append(bag) # add this bag to the queue
        totalBags += int(count) # add the amount of this bag to the total

    # while there are still bags in the queue
    while q:
        cur = q.popleft() # get a bag
        bagsDict = bagsMap2[cur] # get the bags from this bag
        for bag, count in bagsDict.items(): # for each of these bags
            for i in range(int(count)): # add count bags to the queue
                q.append(bag) # add this bag to the queue
            totalBags += int(count) # add the amount of this bag to the totals
    #endregion
    
    # subtract one because we initialized our loop with "shiny bag" to reduce code overhead, but this bag doesnt count by itself
    return len(shinyBags) - 1, totalBags

if __name__ == '__main__':
    year, day = os.path.basename(os.getcwd()), re.findall(r'^.*day(\d+).py$', __file__)[0]
    # getInput(year, day) #NOTE: COMMENT ONCE INPUT FETCHED
    lines = [l.strip() for l in open(f'day{day}input.txt').readlines()]
    part1, part2 = main(lines)
    print(part1, part2)
    # submitAnswer(year, day, 1, part1) #NOTE: UNCOMMENT TO AUTO SUBMIT
    # submitAnswer(year, day, 2, part2) #NOTE: UNCOMMENT TO AUTO SUBMIT

    #region notes
    """
    bool addedBag = false
    bagsMap = dict({}) // holds all the bags, we remove from this as we find bags that lead to shiny
    shiny = set({}) // holds bags that are confirmed to have a path to shiny bags, either directly or indirectly

    1. start by finding all bags that directly hold shiny bags -> add these to shinyBags set({})
        -> remove these bags from the set of all bags (maybe use a queue for all of them and remove as path to shiny is found)
    2. next, find all bags that hold anything in shiny bags (aka shiny directly or 1 away at this point)
        -> remove these from the set of all bags (maybe use a queue for all of them and remove as path to shiny is found)
        -> set added bag to true (surely some bags hold shiny, or the problem would suck. This should always mean we enter the while loop)

    while (addedBag)
        -> addedBag = false
        -> if we add a back, set addedBag to True

    3. keep doing this while we add a new bag to shiny 
        -> if we loop and do not add a new bag, we are done
    
    return len(shiny)
    """
    #endregion notes