#!/usr/bin/env python3

import sys
from collections import defaultdict
from functools import cache
import math
# from numpy import np

with open(sys.argv[1]) as f:
    data = f.read()
lines = data.split("\n")
print("------------------------------------------------------")


expanded_rows = []
iso = "."*len(lines[0])
for (r, line) in enumerate(lines):
    # print(line)
    if line == iso:
        expanded_rows.append(r)
    # for row in expanded:
    #     print(row)

expanded_cols = []

iso = "."*len(lines)
for coli in range(len(lines[0])):
    col = ''.join(line[coli] for line in lines)
    if col == iso:
        expanded_cols.append(coli)

cords = []

for (r, line) in enumerate(lines):
    for (c, ch) in enumerate(line):
        if ch == "#":
            cords.append((c, r))

print(cords)
sm = 0
n = 0
print()

for line in lines:
    print(line)
print()

print(expanded_rows)
print(expanded_cols)

for i in range(len(cords)):
    for j in range(i):
        a = cords[i]
        b = cords[j]
        d = abs(a[0]-b[0])+abs(a[1]-b[1])
        for r in expanded_rows:
            if min(a[1], b[1]) < r < max(a[1], b[1]):
                d += 10**6-1
        for c in expanded_cols:
            if min(a[0], b[0]) < c < max(a[0], b[0]):
                d += 10**6-1
        
        # print()
        # print(i+1, j+1, d)
        sm += d
        n += 1

print(sm)