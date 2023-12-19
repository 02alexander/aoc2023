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

dirs = [1+0j, 0+1j, -1+0j, 0-1j]


def navigate(cost, end):
    visited = set()
    cur = [(0, 0, 0, 0, 0)]
    heapify(cur)
    while len(cur) != 0:
        (dist, cons, dr, posr, posi) = heappop(cur)
        pos = posr + posi*1j
        if (pos, cons, dr) in visited:
            continue
        visited.add((pos, cons, dr))

        if pos == end and cons >= 4:
            return dist
        
        for dir in range(4):
            if cons != 0 and cons < 4 and dir != dr:
                continue
            if (dir-dr)%4 != 2:
                if cons >= 10 and dir == dr:
                    continue
                newdir = dir
                newcons = cons
                if dr != dir:
                    newcons = 0
                newpos = pos+dirs[newdir]
                if newpos not in costs:
                    continue
                newdist = cost[newpos]+dist
                newcons += 1
                heappush(cur, (newdist, newcons, newdir, newpos.real, newpos.imag))


costs = dict()
for (r, line) in enumerate(lines):
    for (c, ch) in enumerate(line):
        costs[c+ 1j*r] = int(ch)

end = len(lines[0])-1+(len(lines)-1)*1j

print(navigate(costs, end))
