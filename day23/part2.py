#!/usr/bin/env python3

import sys
from collections import defaultdict
from heapq import heapify, heappop, heappush
from functools import cache
from itertools import product
import math
import random
from copy import deepcopy
import queue
# 
with open(sys.argv[1]) as f:
    data = f.read().strip()
lines = [line.strip() for line in data.splitlines()]

w = len(lines[0])
h = len(lines)

dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
slopes = {
    "<": 0,
    "v": 1,
    ">": 2,
    "^": 3
}

mp = dict()
for (r, line) in enumerate(lines):
    for (c, ch) in enumerate(line):
        if ch != "#":
            mp[(r,c)] = ch

def unv_neighbours(p, max_dist, mp):
    nbs = []
    for dr, dc in dirs:
        cur = (p[0]+dr, p[1]+dc)
        if cur in max_dist:
            continue
        if cur not in mp:
            continue
        nbs.append(cur)
    return nbs


def nb_conj(start, mp):
    conjd = set()
    # q = [(0, set(), start)]
    q = []
    for nb in unv_neighbours(start, set(), mp):
        q.append((0, set([start]), nb))
    while len(q) > 0:
        d, visited, cur = q[0]
        del q[0]

        if cur in visited:
            continue
        visited = set(visited)
        visited.add(cur)

        nbs = unv_neighbours(cur, visited, mp)
        if len(nbs) > 1:
            conjd.add((d+1, cur))
        elif len(nbs) != 0:
            for nb in nbs:
                q.append((d+1, visited, nb))
    return list(conjd)



def simplify(start, end, mp):
    marked = set()
    graph = defaultdict(set)
    q = [start, end]
    while len(q) > 0:
        cur = q[0]
        del q[0]
        if cur in marked:
            continue
        marked.add(cur)
        for (d,nb) in nb_conj(cur, mp):
            graph[cur].add((d,nb))
            graph[nb].add((d,cur))
            q.append(nb)
    return graph

def longest_path(start, end, graph):
    global max_d
    entry = 0
    q = [(0, entry, start, set())]
    
    entry += 1

    mx = 0
    cnt = 0
    while len(q) > 0:
        d, _, cur, visited = q.pop()
        # d, _, cur, visited = heappop(q)
        if cur in visited:
            continue
        if cur == end:
            cnt += 1
            if cnt % 1000 == 0:
                print(cnt)
                print(mx)
            mx = max(mx, -d)

        visited = set(visited)
        visited.add(cur)
        for (add_d, nb) in graph[cur]:
            q.append((d-add_d, entry, nb, visited))
            entry += 1

    return mx

start = (0, 1)
end = (h-1, w-2)
graph = simplify(start, end, mp) 
print(longest_path(start, end, graph))
