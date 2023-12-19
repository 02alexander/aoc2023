#!/usr/bin/env python3

import sys
from collections import defaultdict
from functools import cache
import math

with open(sys.argv[1]) as f:
    data = f.read()
lines = data.split("\n")
print("------------------------------------------------------")

sm = 0
for line in lines:
    hist = list(map(int, line.split()))
    if hist == [0]*len(hist):
        print("oh oh")
        continue

    layers = [hist]
    is_zero = False
    while not is_zero:
        cur = layers[-1]
        nxt = []
        is_zero = True
        for i in range(0, len(cur)-1):
            nxt.append(cur[i+1]-cur[i])
            if nxt[-1] != 0:
                is_zero = False
        layers.append(nxt)

    layers[-1].insert(0, 0)
    for i in reversed(range(0, len(layers)-1)):
        layers[i].insert(0, layers[i][0]-layers[i+1][0])

    sm += layers[0][0]
    print(layers)
    print()

print(sm)
