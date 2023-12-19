#!/usr/bin/env python3

import sys
from collections import defaultdict
from functools import cache
from itertools import product
import math
# from numpy import np

with open(sys.argv[1]) as f:
    data = f.read().strip()
parts = data.split("\n\n")

def sym(line):
    s = set()
    for i in range(1, len(line)):
        k = 1
        is_sym = True
        while i-k >= 0 and i+k-1 < len(line):
            if line[i-k] != line[i+k-1]:
                is_sym = False
            k += 1
        if is_sym:
            s.add(i)
    return s

sm = 0
for part in parts:
    lines = part.splitlines()
    a = sym(lines[0])
    for line in lines:
        a = a.intersection(sym(line))
    # print(f"a={a}")
 
    for s in list(a):
        sm += s
    if len(a) > 1:
        print(part)
        print()
        print("uh oh")
        
    a = sym(''.join(line[0] for line in lines))
    for c in range(len(lines[0])):
        line = ''.join(line[c] for line in lines)
        a = a.intersection(sym(line))

    for s in list(a):
        sm += 100*s
    if len(a) > 1:
        print("columns")
        print(part)
        print(f"a={a}")
        print()
        print("uh oh")

print(sm)

#22257
#23257 too low