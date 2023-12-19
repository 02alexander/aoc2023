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
lines = data.splitlines()
lines = [ [ch for ch in line] for line in lines ]

def flip(lines):
    return [ list(reversed(line)) for line in lines]

def transpose(lines):
    nw = [ [None]*len(lines) for _ in range(len(lines[0])) ]
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            nw[c][r] = lines[r][c]
    return nw

def tilt(lines):
    nw = []
    for row in lines:
        while True:
            is_done = True
            for i in range(len(row)-1):
                if row[i] == "." and row[i+1] == "O":
                    is_done = False
                    row[i] = "O"
                    row[i+1] = "."
            if is_done:
                break
        nw.append(row)
    return nw

def as_tuple(lines):
    return tuple(tuple(line) for line in lines)

def weight(lines):
    ncols = len(lines[0])
    tot_sm = 0
    for col in lines:
        sm = 0
        cur_weight = ncols
        for i in range(len(col)):
            if col[i] == "O":
                sm += cur_weight
            cur_weight -= 1
        tot_sm += sm
    return tot_sm

def rotate(lines, dr):
    if dr == 0:
        return transpose(lines)
    if dr == 3:
        return flip(lines)
    if dr == 2:
        return flip(transpose(lines))
    if dr == 1:
        return lines

def inv_rotate(lines, dr):
    if dr == 0:
        return transpose(lines)
    if dr == 3:
        return flip(lines)
    if dr == 2:
        return transpose(flip(lines))
    if dr == 1:
        return lines


visited = dict()
cur_dr = 0
loads = []
loop_start = None

stuff = []
while True:
    dr = cur_dr % 4
    # print(cur_dr//4)
    # if cur_dr//4 > 250:
    #     break

    if dr == 0:
        # print(cur_dr//4)
        # for line in lines:
        #     print(''.join(line))
        # print(weight(transpose(lines)))
        # print()
        stuff.append(deepcopy(lines))

    w = weight(transpose(lines))

    rot = rotate(lines, dr)
    l = tilt(rot)
    lines = inv_rotate(l, dr)
    
    tpl = as_tuple(lines)
    
    if cur_dr == 0:
        print("start_weight=", weight(transpose(lines)))
        # for line in lines:
        #     print(lines)

    if dr == 0:
        if tpl in visited and loop_start is None:
            loop_start = visited[tpl]
            loop_len = cur_dr//4 - loop_start
            break
        visited[tpl] = cur_dr//4
        loads.append(w)
        
    cur_dr += 1

for k in range(loop_start, len(loads)):
    idx = ((k-loop_start) % loop_len) + loop_start
    if loads[idx] != loads[k]:
        print("uh oh")
    # print(idx, k)
    

find_n = 1000000000
idx = ((find_n-loop_start) % loop_len) + loop_start
print(idx)
print()
print(loop_start, loop_len)
print(loads)
print(loads[idx])

print(loads[1])
print(loads[1])

#88718

# cols = []
# for c in range(len(lines[0])):
#     col = ''.join(line[c] for line in lines)
#     cols.append(col)

# print(cols)

# nrows = len(cols[0])
# tot_sm = 0
# print()
# for col in cols:
#     sm = 0
#     cur_weight = nrows
#     print(cur_weight)
#     print(col)
#     for i in range(len(col)):
#         if col[i] == "#":
#             cur_weight = nrows-i-1
#         elif col[i] == "O":
#             sm += cur_weight
#             cur_weight -= 1
#     print(sm)
#     print(tot_sm)
#     print()
#     tot_sm += sm

# print(tot_sm)
