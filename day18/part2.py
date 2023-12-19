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

dirs = [(1,0), (0,1), (-1, 0), (0, -1)]
rmap = {
    0: (1,0),
    1: (0, 1),
    2: (-1, 0),
    3: (0, -1),
}

path = []
path_set = set()

cp = (0,0)
for line in lines:
    _dr, _n, other = line.split()
    delta = rmap[int(other[-2])]
    n = int(other[2:-2],base=16)
    cp = (cp[0]+delta[0]*n, cp[1]+delta[1]*n)
    path.append(cp)
    path_set.add(cp)



xs = sorted(list(set( t[0] for t in path )))
ys = sorted(list(set( t[1] for t in path )))

edges = set()
for i in range(len(path)):
    k = (i+1)%len(path)
    edges.add(( path[i], path[k] ))
    edges.add(( path[k], path[i] ))

split_edges = set()
for (src, dst) in edges:
    if src[0] != dst[0]:
        minx = min(src[0], dst[0])
        maxx = max(src[0], dst[0])
        prev = minx
        for x in xs:
            if prev < x <= maxx:
                # print((prev, src[1]), (x, src[1]))
                split_edges.add( ((prev, src[1]), (x, src[1]) ) )
                split_edges.add( ((x, src[1]), (prev, src[1]) ) )
                prev = x
            if x > maxx:
                break
    elif src[1] != dst[1]:
        miny = min(src[1], dst[1])
        maxy = max(src[1], dst[1])
        prev = miny
        for y in ys:
            if prev < y <= maxy:
                split_edges.add( ((src[0], prev), (src[0], y) ) )
                split_edges.add( ((src[0], y), (src[0], prev) ) )
                prev = y
            if y > maxy:
                break
    else:
        print("uh oh")

def crossed_x(xl, xr, ys):
    l = []
    for y in ys:
        l.append( ((xl, y), (xr, y)) in split_edges )
    return l

def crossed_y(yl, yr, xs):
    l = []
    for x in xs:
        l.append( ((x, yl), (x, yr)) in split_edges )
    return l

sm = 0
crossed_xs = []
for i in range(len(xs)):
    k = (i+1)%len(xs)
    xl = xs[i]
    xr = xs[k]
    inside = False
    
    crossed_xs.append(crossed_x(xl, xr, ys))

    for (j, change) in enumerate(crossed_x(xl, xr, ys)[:-1]):
        if change:
            inside = not inside
        
        # change from outside to inside.
        if change and inside:
            sm += abs(xr-xl)

        if inside:
            cury = ys[j] 
            nexty = ys[j+1]
            sm += abs(xl-xr)*abs(nexty-cury)

print()
crossed_ys = []
for i in range(len(ys)):
    k = (i+1)%len(ys)
    yl = ys[i]
    yr = ys[k]
    inside = False
    
    crossed_ys.append(crossed_y(yl, yr, xs))

    for (j, change) in enumerate(crossed_ys[-1][:-1]):
        if change:
            inside = not inside
        
        curx = xs[j]

        # change from outside to inside.
        if change and inside:
            sm += abs(yr-yl)

print(sm+1) # no idea why this +1 makes this work.
        

