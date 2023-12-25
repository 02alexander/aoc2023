#!/usr/bin/env python3

import sys
from collections import defaultdict
from heapq import heapify, heappop, heappush
from functools import cache
from itertools import product
import math
from copy import deepcopy
import queue
import numpy as np
# 
with open(sys.argv[1]) as f:
    data = f.read().strip()
lines = [line.strip() for line in data.splitlines()]

def shortest_path(graph, start, end, removed):
    entry = 0
    q = [(entry, [], start)]
    entry += 1
    visited = set()
    heapify(q)
    while len(q) > 0:
        _, path, cur = heappop(q)
        path = path+[cur]
        if cur in visited:
            continue
        if cur == end:
            return path
        visited.add(cur)
        for conn in graph[cur]:
            if (conn, cur) not in removed:
                heappush(q, (entry, path, conn))
                entry += 1

def count_edges(graph, start, end):
    counter = defaultdict(int)
    for _ in range(4):
        path = shortest_path(graph, start, end, counter)
        if path:
            for i in range(len(path)-1):
                counter[(path[i], path[i+1])] += 1
                counter[(path[i+1], path[i])] += 1
        else:
            return counter
    return "same"

def cnt_edges(graph):
    color = defaultdict()
    vs = list(graph.keys())
    color[vs[0]] = 0
    for i in range(len(vs)):
        print(i)
        for j in range(i):
            start = vs[i]
            end = vs[j]
            if start in color and end in color:
                continue
            # print(start, end)
            cnts = count_edges(graph, start, end)
            if cnts == "same":
                color[start] = color[end]
            else:
                color[start] = 1-color[end]
    return color
graph = defaultdict(list)

for line in lines:
    name, conns = line.split(":")
    conns = list(conns.split())
    graph[name] += conns
    for conn in conns:
        graph[conn].append(name)

color = cnt_edges(graph)
n1 = sum(v for v in color.values())
n2 =sum(1-v for v in color.values())
print(n1, n2)
print(n1*n2)

print(shortest_path(graph, "jqt", "rzs", set([("nvd", "cmg"), ("cmg", "nvd")])))