#PART 1
# ans = 0
# with open("day1input.txt", 'r') as f:
#     lines = f.readlines()
#     for line in lines:
#         ans += int(line.strip()) // 3 - 2
# print(ans)

#PART 2
def main():
    ans = 0
    with open("2019/day1input.txt", 'r') as f:
        lines = f.readlines()
        for line in lines:
            temp = int(line.strip())
            while temp > 0:
                f = fuel(temp)
                if f > 0:
                    ans += f
                    temp = temp // 3 - 2
                else:
                    break
        print(ans)
        
def fuel(num):
    return num // 3 - 2

def tester(temp):
    ans = 0
    while temp > 0:
        f = fuel(temp)
        if f > 0:
            ans += f
            temp = temp // 3 - 2
        else:
            break
    print(ans)


if __name__ == '__main__':
    main()
    # tester(100756)