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

expanded = []
iso = "."*len(lines[0])
for line in lines:
    # print(line)
    if line == iso:
        expanded.append(line)
        expanded.append(line)
    else:
        expanded.append(str(line))
    # for row in expanded:
    #     print(row)

for row in expanded:
    print(row)


cols = []
iso = "."*len(expanded)
for coli in range(len(expanded[0])):
    col = ''.join(line[coli] for line in expanded)
    if col == iso:
        cols.append(col)
        cols.append(col)
    else:
        cols.append(col)

print(cols)

rows = []
for rowi in range(len(cols[0])):
    row = ''.join(col[rowi] for col in cols)
    rows.append(row)


cords = []

for (r, row) in enumerate(rows):
    for (c, ch) in enumerate(row):
        if ch == "#":
            cords.append((c, r))

print()
for col in cols:
    print(col)
print()

print(cords)
sm = 0
n = 0
for i in range(len(cords)):
    for j in range(i):
        a = cords[i]
        b = cords[j]
        d = abs(a[0]-b[0])+abs(a[1]-b[1])
        print(i+1, j+1, d)
        sm += d
        n += 1

print(n)
print(sm)
print()


# for row in rows:
#     print(row)

