import itertools as iter
import collections as col
import hashlib as hash
import math
import json
import re

def main():
    #NOTE: this is the original trash code that was used while racing for completion time
    #region trash
    # with open("day2input.txt", 'r') as f:
    #     strippedLines = [x.strip() for x in f]
    #     res = 0
    #     for x in strippedLines:
    #         digits = x.split("-")
    #         digits = [x.split(" ") for x in digits]
    #         d1 = int(digits[0][0])
    #         d2 = int(digits[1][0])
    #         char = digits[1][1][:1]
    #         password = digits[1][2]
    #         # count = password.count(char)
    #         # if count >= d1 and count <= d2:
    #         #     res +=1
    #         if password[d1-1] == char and password[d2-1] != char:
    #             res += 1
    #         elif password[d1-1] != char and password[d2-1] == char:
    #             res += 1
    # print(res)
    #endregion

    #better solution with regex for parsing
    good1, good2 = 0, 0
    f = open("day2input.txt").read()
    res = re.findall("([0-9]+)-([0-9]+) (\w): (\w+)", f)
    for i in range(len(res)):
        n1, n2, char, password = int(res[i][0]), int(res[i][1]), res[i][2], res[i][3]
        count = password.count(char)
        if count >= n1 and count <= n2:
            good1 +=1
        if (password[n1-1] == char and password[n2-1] != char) or (password[n1-1] != char and password[n2-1] == char):
            good2 += 1
    print(good1, good2)

if __name__ == '__main__':
    main()
