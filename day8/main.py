#!/usr/bin/env python3

import sys
from collections import defaultdict
from functools import cache
import math

with open(sys.argv[1]) as f:
    data = f.read()
lines = data.split("\n")
print("------------------------------------------------------")

def tm(graph, start):
    i = 0
    cur = start
    visited = {}
    finish_time = None
    cycle_time = None
    while True:
        idx = i%len(inst)
        i += 1
        if (cur, idx) in visited:
            cycle_time = i-visited[(cur, idx)]
            break
        visited[(cur, idx)] = i
        
        if cur[2] == "Z":
            finish_time = i-1
        dirs = graph[cur]
        if inst[idx] == "L":
            cur = dirs[0]
        else:
            cur = dirs[1]
        
    return (finish_time, cycle_time)

inst = lines[0].strip()
graph = {}
for line in lines[2:]:
    parts = line.split()
    src = parts[0]
    left = parts[2][1:-1]
    right = parts[3][:-1]
    graph[src] = (left, right)

timings = []
curs = []
for v in graph.keys():
    if v[2] == "A":
        timings.append(tm(graph, v))
        curs.append(v)

lcm = math.lcm(*(t[0] for t in timings))
print(lcm)
