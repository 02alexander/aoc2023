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


deltas = {
    "|": (0, 1),
    "-": (1, 0),
    "L": (1, -1),
    "J": (-1, -1),
    "7": (-1, 1),
    "F": (1, 1),
}

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
print(pipes)
for (stc, str) in start_dir:
    st = (start[0],stc+start[1]+str)
    print(st)
    i = 0
    prev = start
    cur = st
    while True:
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
            print()
            print(ch)
            print(prev, cur)
            print(f"src = {src} dst = {dst}")
            if prev == src:
                prev = cur
                cur = dst
            elif prev == dst:
                prev = cur
                cur = src
            else:
                i = 0
                print("loop")
                break
            print(prev, cur)
        elif cur == "S":
            print("done")
            break
        else:
            print("invalid")
            break
    print(i)
    mx = max(mx, i//2)

print(mx)

# graph = defaultdict(set)
# def connect(a, b):
#     graph[a].add(b)
#     graph[b].add(a)

# start = None
# for (r, line) in enumerate(lines):
#     for (col, ch) in enumerate(line):
#         cur = (col, r)
#         if ch == "S":
#             start = (col, r)
#         elif ch == "|":
#             connect(cur, (col, r+1))
#             connect(cur, (col, r-1))
#         if ch == "-":
#             connect(cur, (col-1, r))
#             connect(cur, (col+1, r))            
#         if ch == "L":
#             connect(cur, (col-1, r))
#             connect(cur, (col, r+1))
            
#         if ch == "J":
#             connect(cur, (col, r-1))
#             connect(cur, (col-1, r))
#         if ch == "7":
#             connect(cur, (col, r-1))
#             connect(cur, (col+1, r))
#         if ch == "F":
#             connect(cur, (col, r+1))
#             connect(cur, (col+1, r))
    

    

# mx = 0
# print(graph)
# for startss in graph[start]:

#     prev = start
#     cur = startss
#     print(cur)
#     i = 0
#     while cur != start and i < 5:
#         print()
#         i += 1
#         mx = max( abs(cur[0]-start[0])+abs(cur[1]-start[1]), mx )
#         print(prev, cur)
#         print(graph[cur])
#         for nb in graph[cur]:
#             if nb != prev:
#                 prev = cur
#                 cur = nb

# print(mx)

