#!/usr/bin/env python3

import sys
from collections import defaultdict
from heapq import heapify, heappop, heappush
from functools import cache
from itertools import product
import math
from copy import deepcopy
import queue
import numpy as np
# 
with open(sys.argv[1]) as f:
    data = f.read().strip()
lines = [line.strip() for line in data.splitlines()]

def intersects(p1, v1, p2, v2):
    mat = np.array([
        [v1[0], -v2[0]],
        [v1[1], -v2[1]]
    ])
    if abs(np.linalg.det(mat)) > 0.001:
        solution = np.linalg.solve(mat, (p2-p1)[:2])
        if solution[0] < 0 or solution[1] < 0:
            return None
        return p1 + solution[0]*v1
    return None

flakes = []

for line in lines:
    line = line.replace(",", "")
    p, v = line.split("@")
    p = list(map(int, p.split()))
    v = list(map(int, v.split()))
    flakes.append((np.array(p),np.array(v)))

# minx = 7
# maxx = 27
# miny = 7
# maxy = 27

minx = miny = 200000000000000
maxx = maxy = 400000000000000

cnt = 0
for i in range(len(flakes)):
    for j in range(i):
        p = intersects(*flakes[i], *flakes[j])
        if p is not None:
            # print(i, j, p)
            if minx <= p[0] <= maxx and miny <= p[1] <= maxy:
                # print("counts!")
                cnt += 1

print(cnt)