#!/usr/bin/env python3

import sys
from collections import defaultdict
from heapq import heapify, heappop, heappush
from functools import cache
from itertools import product
import math
from copy import deepcopy
import numpy as np
# 
with open(sys.argv[1]) as f:
    data = f.read().strip()
lines = [line.strip() for line in data.splitlines()]

print(lines)

def cubes(start, end):
    for i in range(3):
        if start[i] != end[i]:
            cbs = []
            si = min(end[i], start[i])
            ei = max(end[i], start[i])
            for k in range(si, ei+1):
                cb = list(start)
                cb[i] = k
                cbs.append(tuple(cb))
            return cbs
    return [start]

def lower(cubes, dz):
    return [(cb[0], cb[1], cb[2]+dz) for cb in cubes]


bricks = []
deps = defaultdict(list)


maxx = 0
maxy = 0
maxz = 0
for line in lines:
    start, end = line.split("~")
    start = tuple(map(int, start.split(',')))
    end = tuple(map(int, end.split(',')))
    maxx = max(maxx, start[0], end[0])
    maxy = max(maxy, start[1], end[1])
    maxz = max(maxz, start[2])
    maxz = max(maxz, end[2])
    bricks.append(cubes(start, end))

print(maxx, maxy, maxz)
stable = set()
occupied = -1*np.ones((maxx+1,maxy+1,maxz+1))
print(occupied)

for id, cbs in enumerate(bricks):
    for cb in cbs:
        print(cb)
        occupied[*cb] = id

all_stable = False
while not all_stable:
    all_stable = True
    for (id, cbs) in enumerate(bricks):
        if id in stable:
            continue
        # print()
        # print(id)
        # print(occupied)
        all_stable = False
        lowered = lower(cbs, -1)
        can_drop = True
        for cb in lowered:
            if cb[2] < 0:
                can_drop = False
                stable.add(id)
            elif occupied[*cb] != -1 and occupied[*cb] != id:
                if occupied[*cb] in stable:
                    stable.add(id)
                can_drop = False
        if can_drop:

            for cb in cbs:
                if occupied[*cb] != id:
                    print("uh oh", cb)                
                occupied[*cb] = -1
            for cb in lowered:
                occupied[*cb] = id
                if occupied[*cb] != id and occupied[*cb] != -1:
                    print("uh oh", cb)
            bricks[id] = lowered


print(occupied)
            
deps = defaultdict(set)
for x in range(maxx+1):
    for y in range(maxy+1):
        for z in range(maxz):
            id = occupied[x,y,z]
            if id != -1:
                above = occupied[x, y, z+1]
                if above != id and above != -1:
                    deps[int(above)].add(int(id))

crucial = set()

for id, dep in deps.items():
    if len(dep) == 1:
        crucial.add(next(iter(dep)))

cnt = 0
for id in range(len(bricks)):
    if id not in crucial:
        cnt += 1

print(cnt)

# for (id, cbs) in enumerate(bricks):
#     for cube in cbs:
#         for j in range(cube[2]+1, maxz+1):
#             cube = (cube[0], cube[1], j)
#             done = False
#             for i in range(len(bricks)):
#                 if cube in bricks[i]:
#                     deps[i].append(id)
#                     done = True
#                     break
#             if done:
#                 break
                    
# print(deps)