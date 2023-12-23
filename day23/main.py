#!/usr/bin/env python3

import sys
from collections import defaultdict
from heapq import heapify, heappop, heappush
from functools import cache
from itertools import product
import math
from copy import deepcopy
import queue
import numpy as ne
# 
with open(sys.argv[1]) as f:
    data = f.read().strip()
lines = [line.strip() for line in data.splitlines()]

w = len(lines[0])
h = len(lines)

dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
slopes = {
    "<": 0,
    "v": 1,
    ">": 2,
    "^": 3
}

mp = dict()
for (r, line) in enumerate(lines):
    for (c, ch) in enumerate(line):
        mp[(r,c)] = ch

def solve(start, end, mp, depth=0):
    global max_d
    nxt = [(0, set(), start)]
    mx = 0
    while len(nxt) > 0:
        d, visited, cur = nxt[0]
        del nxt[0]
        if cur in visited:
            continue
        if cur not in mp:
            continue
        if cur in mp and mp[cur] == "#":
            continue
        if cur == end:
            print("reached end!")
            mx = max(mx, d+1)
        visited = set(visited)
        visited.add(cur)
        # print(cur)
        for i in range(4):
            c = mp[cur]
            if c in slopes:
                if i != slopes[c]:
                    continue
            
            dr, dc = dirs[i]
            new = (cur[0]+dr, cur[1]+dc)
            nxt.append((d+1, visited, new))
            
    return mx

# print(f'end={(w-2, h-1)}')
d = solve((0, 1), (h-1, w-2), mp)-1
print(d)

#2167