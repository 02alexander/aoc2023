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


def comp_dists(mp, start):
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    dsts = {}
    nxt = [(0, start)]
    heapify(nxt)
    while len(nxt) > 0:
        d, cur = heappop(nxt)
        if cur in dsts:
            continue
        dsts[cur] = d
        for (dr, dc) in dirs:
            n = (dr+cur[0], dc+cur[1])
            if n not in mp:
                continue
            heappush(nxt, (d+1, n))
    return dsts


mp = {}

start = None

repeat = 0
w = len(lines[0])
h = len(lines)
for (row, line) in enumerate(lines):
    for (col, ch) in enumerate(line):
        if ch == ".":
            for k in range(0, repeat*2+1):
                mp[(row+h*k,col+w*repeat)] = ch
        elif ch == "S":
            start = (row+h*repeat,col+w*repeat)


dsts = comp_dists(mp, start)
cnt = 0
mx = 500
for cord, d in dsts.items():
    if d <= mx and (d-mx) % 2 == 0:
        cnt +=1
print(cnt)


