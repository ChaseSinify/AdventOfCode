# part 1
# with open("2015/day1input.txt", 'r') as f:
#     stringy = f.readlines()[0].strip()
#     res = 0
#     for c in stringy:
#         if c == '(':
#             res += 1
#         else: #')'
#             res -= 1
#     print(res)

# part 2
with open("2015/day1input.txt", 'r') as f:
    stringy = f.readlines()[0].strip()
    res = 0
    index = 1
    for c in stringy:
        if c == '(':
            res += 1
        else: #')'
            res -= 1
        if res < 0:
            break
        else:
            index += 1
    print(index)