"""
You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had written the password on a sticky note, but someone threw it out.

However, they do remember a few key facts about the password:

    It is a six-digit number.
    The value is within the range given in your puzzle input.
    Two adjacent digits are the same (like 22 in 122345).
    Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).

Other than the range rule, the following are true:

    111111 meets these criteria (double 11, never decreases).
    223450 does not meet these criteria (decreasing pair of digits 50).
    123789 does not meet these criteria (no double).

How many different passwords within the range given in your puzzle input meet these criteria?
INPUT: 236491 - 713787
"""
#PART 1
# valid = 0
# for i in range(236491, 713787 + 1): # not sure if needs to be inclusive
#     lessy = True
#     adjacent = False
#     strnum = str(i)
#     for x in range(len(strnum)-1):
#         if int(strnum[x]) > int(strnum[x+1]):
#             lessy = False
#         if strnum[x] == strnum[x+1]:
#             adjacent = True
#     if lessy and adjacent:
#         valid += 1
# print(valid)

#PART 2
valid = 0
for i in range(236491, 713787 + 1): # not sure if needs to be inclusive
    lessy = True
    adjacent = False
    strnum = str(i)
    for x in range(len(strnum)-1):
        if int(strnum[x]) > int(strnum[x+1]):
            lessy = False
        if strnum[x] == strnum[x+1] and strnum.count(strnum[x]) == 2:
            adjacent = True
    if lessy and adjacent:
        valid += 1
print(valid)