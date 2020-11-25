#PART1
# maybe we cant rely on order, since in main set some are not in map other than COM,
# but we know everyone but COM has to orbit someone
#NOTE: the above is true, you cannot rely on order
# with open('2019/day6input.txt', 'r') as f:
#     orbits = [x.strip() for x in f.readlines()]
#     # print(orbits)
#     orbitMap = {} #store planet as key, direct orbits as value
#     #manually add COM, which is the only exception to the logic
#     orbitMap['COM'] = 0
#     while orbits:
#         # take the first element
#         orbited, orbiter = orbits.pop(0).split(')')

#         #if this orbited planet isnt already in the map, append it to back
#         if orbited not in orbitMap:
#             orbits.append(f'{orbited}){orbiter}')
        
#         #if the orbited planet is in map, add this new orbiter with orbited + 1
#         else:
#             orbitMap[orbiter] = orbitMap[orbited] + 1
             
#     totalOrbits = 0
#     for v in orbitMap.values():
#         totalOrbits += v
#     print(totalOrbits)

#PART2
#NOTE: the shortest path must be a path from YOU that intercepts a planet that is on the path from
#      SAN -> COM. We can store the full list of paths for YOU and SAN to COM, and find the shortest
#      connection point by checking all of them
r"""
                          YOU
                         /
        G - H       J - K - L
       /           /
COM - B - C - D - E - F
               \
                I - SAN
"""
import math
with open('2019/day6input.txt', 'r') as f:
    orbits = [x.strip() for x in f.readlines()]
    # print(orbits)
    orbitMap = {} #store planet as key, direct orbits as value
    #manually add COM, which is the only exception to the logic
    orbitMap['COM'] = None
    while orbits:
        # take the first element
        orbited, orbiter = orbits.pop(0).split(')')

        #if this orbited planet isnt already in the map, append it to back
        if orbited not in orbitMap:
            orbits.append(f'{orbited}){orbiter}')
        
        #if the orbited planet is in map, add this new orbiter with orbited + 1
        else:
            orbitMap[orbiter] = orbited
            # print(orbitMap[orbiter])
    
    san = orbitMap['SAN']
    sanToCom = ['SAN', san]
    while san != None:
        san = orbitMap[san]
        sanToCom.append(san)
    # print(sanToCom)
    # if len(sanToCom) == len(set(sanToCom)): #checking that this is actually a unique path
    #     print("TRUE")
    you = orbitMap['YOU']
    youToCom = ['YOU', you]
    while you != None:
        you = orbitMap[you]
        youToCom.append(you)
    # print(youToCom)
    # if len(youToCom) == len(set(youToCom)): #checking that this is actually a unique path
    #     print("TRUE")
    
    for p in youToCom:
        if p in sanToCom:
            print(youToCom.index(p) + sanToCom.index(p) - 2)
            break
    