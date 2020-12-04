import itertools as iter
import collections as col
import hashlib as hash
import math
import json
import re

def passports(lines):
    valid = 0
    needed = set({'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}) #cid
    passport = set({})
    for line in lines:
        if line == "":
            if 'cid' in passport:
                passport.remove('cid')
            if passport == needed:
                valid += 1
            passport.clear()
            continue

        split = line.split()
        for s in split:
            item = s.split(':')
            # passport.add(item[0])
            tick = item[0]
            value = item[1]
            if tick == 'byr':
                if len(value) == 4 and int(value) >= 1920 and int(value) <= 2002:
                    passport.add(tick)
            elif tick == 'iyr':
                if len(value) == 4 and int(value) >= 2010 and int(value) <= 2020:
                    passport.add(tick)
            elif tick == 'eyr':
                if len(value) == 4 and int(value) >= 2020 and int(value) <= 2030:
                    passport.add(tick)
            elif tick == 'hgt':
                if value[-2:] == 'cm':
                    if int(value[:-2]) >= 150 and int(value[:-2]) <= 193:
                        passport.add(tick)
                elif value[-2:] == 'in':
                    if int(value[:-2]) >= 59 and int(value[:-2]) <= 76:
                        passport.add(tick)
            elif tick == 'hcl':
                if re.findall(r'^#[0-9a-fA-F]{6}$', value):
                    passport.add(tick)
            elif tick == 'ecl':
                if value in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
                    passport.add(tick)
            elif tick == 'pid':
                if re.findall(r'^[0-9]{9}$', value):
                    passport.add(tick)

    #file exits on a new line before we finally check the last passport value == needed zzz == off by 1
    if passport == needed:
        valid += 1

    return valid

if __name__ == '__main__':
    lines = [x.strip() for x in open("2020/day4input.txt", 'r').readlines()]
    print(passports(lines))