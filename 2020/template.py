import itertools as iter
import collections as col
import hashlib as hash
import math
import json
import re

#TEMPLATE CODE---------------------------------------------------------------------------------------------------------------------------------------------------
def parseInput():
    #INPUT PARSING
    f = open("day2input.txt")
    rawLines = [x for x in f.readlines()]
    strippedLines = [x.strip() for x in rawLines]
    firstLine = strippedLines[0]
    singleLineCommaSepRaw = [x for x in strippedLines[0].split(',')]
    singleLineCommaSepStripped = [x.strip() for x in singleLineCommaSepRaw]
    multiLineCommaSepRaw = [x.split(',') for x in strippedLines]
    multiLineCommaSepStripped = []
    intLines = []
    floatLines = []
    stringLines = []
    commaInts = []
    commaFloats = []
    commaIntsLines = []
    commaFloatsLines = []

    for x in multiLineCommaSepRaw:
        temp = []
        for y in x:
            temp.append(y.strip())
        multiLineCommaSepStripped.append(temp)

    # try to parse ints, floats, etc. that may be on SINGLE LINES
    try:
        intLines = [int(x) for x in strippedLines]
    except:
        try:
            floatLines = [float(x) for x in strippedLines]
        except:
            stringLines = [str(x) for x in strippedLines]

    # try to parse comma sep into ints and floats for SINGLE LINE and MULTIPLE LINES
    if len(rawLines) == 1:
        try: 
            commaInts = [int(x) for x in firstLine.split(',')]
        except ValueError:
            try:
                commaFloats = [float(x) for x in firstLine.split(',')]
            except:
                pass
    else:
        try: 
            for x in strippedLines:
                temp = []
                for y in x.split(','):
                    temp.append(y.strip())
                commaIntsLines.append(temp)
        except ValueError:
            try:
                for x in strippedLines:
                    temp = []
                    for y in x.split(','):
                        temp.append(y.strip())
                    commaIntsLines.append(temp)
            except:
                pass
                
    # print(intLines)
    # print(floatLines)
    # print(stringLines)
    # if intLines: print("int")
    # if floatLines: print("float")
    # if stringLines: print("string")

    # print(commaInts)
    # print(commaFloats)
    # print(commaIntsLines)
    # print(commaFloatsLines)

    #TODO: Return the only case that passed a parse attempt, else default to just raw string information
    
    #TODO: add point parsing i.e. int, int on each line

#TODO: make this only relative to up, down, left, right--always that order
"""
Returns a single int increment 'step' in any direction, needs update to take more params and more than single steps
"""
def step(direction):
    vert = 0
    horz = 0
    if dir[0] == 'UP':
        vert += int(dir[1:])
    elif dir[0] == 'DOWN':
        vert -= int(dir[1:])
    elif dir[0] == 'L':
        horz -= int(dir[1:])
    elif dir[0] == 'R':
        horz += int(dir[1:])
    return (horz, vert)