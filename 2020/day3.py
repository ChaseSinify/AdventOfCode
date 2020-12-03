def trees(hill, right, down):
    tree, r, c, l = 0, 0, 0, len(hill[0])
    while r < len(hill):
        tree += hill[r][c % l] == "#"
        r += down
        c = (c + right) % l
    return tree

if __name__ == '__main__':
    lines = [x.strip() for x in open("day3input.txt").readlines()]
    print(trees(lines, 3, 1)) #part 1
    print(trees(lines, 1, 1) * trees(lines, 3, 1) * trees(lines, 5, 1) * trees(lines, 7, 1) * trees(lines, 1, 2)) #part 2