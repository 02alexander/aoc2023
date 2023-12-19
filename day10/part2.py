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

print(lines)
width = len(lines[0])
height = len(lines)


deltas = {
    "|": (0, 1),
    "-": (1, 0),
    "L": (1, -1),
    "J": (-1, -1),
    "7": (-1, 1),
    "F": (1, 1),
}

def connect(a, b, grid):
    src = (a[0]*2, a[1]*2)
    dst = (b[0]*2, b[1]*2)
    mid = (a[0]+b[0], a[1]+b[1])
    grid[src[0]][src[1]] = "#"
    grid[dst[0]][dst[1]] = "#"
    grid[mid[0]][mid[1]] = "#"

pipes = {}
start = None


for (r, line) in enumerate(lines):
    for (col, ch) in enumerate(line):
        if ch in deltas:
            pipes[(col, r)] = ch
        elif ch == "S":
            start = (col, r)

start_dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
mx = 0
border = None
final_grid = None
for (stc, str) in start_dir:
    grid = []
    for _ in range(width*2):
        grid.append(["."]*(height*2+1))
    # grid = []*(width*2+1)

    cur_border = set()
    st = (start[0],stc+start[1]+str)
    i = 0
    prev = start
    cur = st
    while True:
        connect(prev, cur, grid)
        i += 1
        if cur in pipes:
            ch = pipes[cur]
            if ch == "|":
                src = (cur[0],cur[1]-1)
                dst = (cur[0],cur[1]+1)
            elif ch == "-":
                src = (cur[0]-1,cur[1])
                dst = (cur[0]+1,cur[1])
            else:
                src = (cur[0]+deltas[ch][0],cur[1])
                dst = (cur[0],cur[1]+deltas[ch][1])

            if prev == src:
                prev = cur
                cur = dst
            elif prev == dst:
                prev = cur
                cur = src
            else:
                print(ch)
                print("uh oh")
                i = 0
                break
        elif cur == start:
            print("done")
            final_grid = grid
            break
        else:
            print(ch)
            print("invalid")
            break
    print(i)
    mx = max(mx, i//2)

def fill_inside(start_point, grid):
    nbs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    filled = set()
    cur = start_point
    is_inner = True
    done = False
    nxt = [cur]
    while len(nxt) != 0:
        current = nxt.pop()
        done = True
        for (dc, dr) in nbs:
            cur = current
            # print()
            # print(cur)
            cur = (cur[0]+dc, cur[1]+dr)
            # print(cur)
            if cur in filled:
                continue
            if cur[0] < 0 or cur[1] < 0 or cur[0] == width*2 or cur[1] == height*2:
                is_inner = False
                continue

            if grid[cur[0]][cur[1]] == "#":
                continue

            filled.add(cur)
            nxt.append(cur)
            done = False
    return (filled, is_inner)

grid = []
for _ in range(width*2):
    grid.append(["."]*(height*2+1))

cnt = 0
visited = set()
for startc in range(width*2):
    for startr in range(height*2):
        if (startc, startr) not in visited:
            if final_grid[startc][startr] == "#":
                continue
            (s, is_inner) = fill_inside((startc, startr), final_grid)
            visited = visited.union(s)
            if is_inner:
                for (c, r) in s:
                    if (c % 2) == 0 and (r%2)==0:
                        grid[c][r] = "#"
                        cnt += 1


for startr in range(height*2):
    for startc in range(width*2):
        print(final_grid[startc][startr], end="")
    print()

print()

for startr in range(height*2):
    for startc in range(width*2):
        print(grid[startc][startr], end="")
    print()

print(cnt)
