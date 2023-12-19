#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
    lines = [line.strip() for line in f.readlines()]
print("-------------------------------------------")

sm = 0
ncards = 1
copies = [1]*len(lines)
copies[0]=1
for (i, line) in enumerate(lines):
    _, res = line.split(': ')
    (hav, win) = res.split("| ")
    hav = set([int(p) for p in hav.split()])
    win = set([int(p) for p in win.split()])
    ins = hav.intersection(win)

    for k in range(i+1, min(len(lines), i+len(ins)+1)):
        copies[k] += copies[i]

    if len(ins) >= 1:
        sm += 2**(len(ins)-1)

print(sm)
print(sum(copies))