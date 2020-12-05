import itertools as iter
import collections as col
import hashlib as hash
import math
import json
import re

from autoInput import getInput, startInputClock
from autoSubmit import submitAnswer

def password(lines):
    id, password, i = lines[0], "", 0
    while len(password) < 8:
        input = f'{id}{i}'
        result = hash.md5(input.encode()).hexdigest()
        if str(result)[:5] == '00000':
            print(result)
            password += str(result)[5]
        i += 1
    return password

if __name__ == '__main__':
    lines = [x.strip() for x in open("day5input.txt").readlines()]
    # submitAnswer(2016, 5, 1, password(lines))
    # getInput(2016, 5) 