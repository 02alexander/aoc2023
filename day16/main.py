#!/usr/bin/env python3

import sys
from collections import defaultdict
from functools import cache
from itertools import product
import math
from copy import deepcopy
# from numpy import np

with open(sys.argv[1]) as f:
    data = f.read().strip()
lines = [line.strip() for line in data.splitlines()]

# right up left down
dirs = [1+0j, 0+1j, -1+0j, 0-1j]

table = {

    (2, "/"): (1),
    (1, "/"): (2),
    (0, "/"): (3),
    (3, "/"): (0),
    

    (2, "\\"): (3),
    (3, "\\"): (2),
    (0, "\\"): (1),
    (1, "\\"): (0),
}

split_in = {
    (0, "|"): (1, 3),
    (2, "|"): (1, 3),
    
    (1, "-"): (0, 2),
    (3, "-"): (0, 2),
}

w = len(lines[0])
h = len(lines)

def solve(startp, startd):
    visited = defaultdict(list)

    beams = [(startp, startd), ]

    while len(beams) > 0:

        new_beams = []
        for (p, di) in beams:
            p += dirs[di]
            # print(p)

            if p.real < 0 or p.real >= w or p.imag < 0 or p.imag >= h:
                continue

            if p in visited and di in visited[p]:
                continue

            visited[p].append(di)
            ch = lines[int(p.imag)][int(p.real)]
            if ch != ".":
                if (di, ch) in table:
                    di = table[(di,ch)]
                    new_beams.append((p, di))
                elif (di,ch) in split_in:
                    t = split_in[(di,ch)]
                    new_beams.append((p, t[0]))
                    new_beams.append((p, t[1]))
                else:
                    new_beams.append((p, di))
            else:
                new_beams.append((p, di))
        beams = new_beams
    cnt = 0
    for _ in visited:
        cnt += 1
    return cnt

mx = 0
for row in range(h):
    startp = -1+row*1j
    d = 0
    mx = max(mx, solve(startp, d))
    startp = w+row*1j
    d = 2
    mx = max(mx, solve(startp, d))

for col in range(w):
    startp = col-1j
    d = 1
    mx = max(mx, solve(startp, d))
    startp = col+h*1j
    d = 3
    mx = max(mx, solve(startp, d))

sol1 = solve(-1+0j, 0)
print(f"part 1 {sol1}")
print(f"part 2 {mx}")
