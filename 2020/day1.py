def main():
    with open("day1input.txt", 'r') as f:
        lines = [x.strip() for x in f.readlines()]
        for i in lines:
            for j in lines:
                for k in lines:
                    if int(i) + int(j) + int(k) == 2020:
                        print(int(i) * int(j) * int(k))

if __name__ == '__main__':
    main()