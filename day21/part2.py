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
repeat = 5
mx = 26501365

w = len(lines[0])
h = len(lines)
print(w, h)
for (row, line) in enumerate(lines):
    for (col, ch) in enumerate(line):
        if ch == "." or ch == "S":
            for k in range(0, repeat*2+1):
                for j in range(0, repeat*2+1):
                    mp[(row+h*k,col+w*j)] = '.'
        if ch == "S":
            start = (row+h*repeat,col+w*repeat)

#assume nsteps % 2 == 1
def solve_quad(offset, nsteps, mx):
    if offset > mx:
        return 0

    if (offset - mx) % 2 == 0:
        m = 1+(mx-offset)//nsteps
        m = (m+1)//2
        return (2*m*(m+1))//2-m
    else:
        m = 1+(mx-offset)//nsteps
        m = m//2
        return (2*m*(m+1))//2

#assume nsteps % 2 == 1
def solve_line(offset, nsteps, mx):
    if offset > mx:
        return 0
    if (offset - mx) % 2 == 0:
        m = 1+(mx-offset)//nsteps
        return (m+1)//2
    else:
        m = 1+(mx-offset)//nsteps
        return m//2


diff = w
dsts = comp_dists(mp, start)
dirs = [(1,0), (0, 1), (-1 ,0), (0, -1)]
diags = [(1,1), (-1, 1), (-1, -1), (1, -1)]

cnt = 0

for row in range(h):
    for col in range(w):
        p = (row, col)
        if p not in dsts:
            continue

        quad_sm = 0
        for (dr, dc) in diags:
            quadp = (p[0]+(repeat+dr)*h, p[1]+(repeat+dc)*w)
            quad_sm += solve_quad(dsts[quadp], diff, mx) 
        linsm = 0
        for (dr, dc) in dirs:
            v = 5
            for k in range(1, v):
                lp = (p[0]+(repeat+k*dr)*h, p[1]+(repeat+k*dc)*w)
                if lp in dsts and dsts[lp] <= mx and (mx-dsts[lp])% 2 == 0:
                    linsm += 1
            lp = (p[0]+(repeat+v*dr)*h, p[1]+(repeat+v*dc)*w)
            if lp in dsts:
                linsm += solve_line(dsts[lp], diff, mx)

        init_sm = 0
        if (row, col) in dsts:
            r = row+h*repeat
            c = col+w*repeat
            d = dsts[(r, c)]
            if d <= mx and (mx - d) % 2 == 0:
                init_sm += 1

        cnt += quad_sm + linsm + init_sm

print(f"{cnt}")
