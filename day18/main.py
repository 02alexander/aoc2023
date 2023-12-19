#!/usr/bin/env python3

import sys
from collections import defaultdict
from heapq import heapify, heappop, heappush
from functools import cache
from itertools import product
import math
from copy import deepcopy
# from numpy import np

with open(sys.argv[1]) as f:
    data = f.read().strip()

lines = [line.strip() for line in data.splitlines()]



def fill_inside(start_point, grid):
    nbs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    filled = set()
    cur = start_point
    is_inner = True
    done = False
    nxt = [cur]
    while len(nxt) != 0:
        current = nxt.pop()
        done = True
        for (dc, dr) in nbs:
            cur = current
            cur = (cur[0]+dc, cur[1]+dr)
            if cur in filled:
                continue
            if cur[0] < minx or cur[1] < miny or cur[0] > maxx or cur[1] > maxy:
                is_inner = False
                continue

            if cur in grid:
                continue

            filled.add(cur)
            nxt.append(cur)
            done = False
    return (filled, is_inner)

dirs = [(1,0), (0,1), (-1, 0), (0, -1)]
rmap = {
    "R": (-1,0),
    "L": (1, 0),
    "U": (0, -1),
    "D": (0, 1),
}

path = set()

cp = (0,0)
for line in lines:
    dr, n, other = line.split()
    n = int(n)
    delta = rmap[dr]
    for _ in range(n):
        cp = (cp[0]+delta[0], cp[1]+delta[1])
        path.add(cp)
    

nodes = list(path)
minx = min(t[0] for t in nodes)
maxx = max(t[0] for t in nodes)
miny = min(t[1] for t in nodes)
maxy = max(t[1] for t in nodes)

visited = set()
inner = set()
print(minx, maxx)
print(miny, maxy)
for x in range(minx, maxx+1):
    for y in range(miny, maxy+1):
        if (x,y) in visited:
            continue
        print(x,y)
        print(visited)
        (filled, is_inner) = fill_inside((x,y), path)
        visited = visited.union(filled)
        if is_inner:
            inner = inner.union(filled)

print(len(inner)+len(nodes))
    
