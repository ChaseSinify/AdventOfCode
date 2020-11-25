import math
from os import close

# this isnt just points intersections...
# the lines cross without points being the same
# however, we can just trace the "line" from p1
# and see if any point on it is in p2,
# calculate distance just like before, and done

def main():
    with open("2019/day3input.txt", 'r') as f:

        lines = f.readlines()
        first = [x.strip() for x in lines[0].split(',')]
        second = [x.strip() for x in lines[1].split(',')]

        points1 = []
        points2 = []

        # print(segment1)

        h1 = 0
        v1 = 0
        for dir in first:
            h, v = step(dir)
            h1 += h
            v1 += v
            points1.append((h1, v1))

        h2 = 0
        v2 = 0
        for dir in second:
            h, v = step(dir)
            h2 += h
            v2 += v
            points2.append((h2, v2))  
    
        #NOTE: a point is on line if L2x1 <= L1x1 == L1x2 <= L2X2 
        #       AND L1y1 <= L2y1 == L2y2 <= L1y2
        #       OR INVERSE OF THE ABOVE
        """ 
        o == center
        X = intersection
        ...........
        .+-----+...
        .|.....|...
        .|..+--X-+.
        .|..|..|.|.
        .|.-X--+.|.
        .|..|....|.
        .|.......|.
        .o-------+.
        ...........

        """
    
        
def step(dir):
    vert = 0
    horz = 0
    if dir[0] == 'U':
        vert += int(dir[1:])
    elif dir[0] == 'D':
        vert -= int(dir[1:])
    elif dir[0] == 'R':
        horz += int(dir[1:])
    elif dir[0] == 'L':
        horz -= int(dir[1:])
    return (horz, vert)

def manhattan(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

if __name__ == '__main__':
    main()
        