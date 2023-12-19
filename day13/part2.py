#!/usr/bin/env python3

import sys
from collections import defaultdict
from functools import cache
from itertools import product
from copy import deepcopy
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

def find_refl(lines):
    a = sym(lines[0])
    for line in lines:
        a = a.intersection(sym(line))
    # print(f"a={a}")
 
    if len(a) > 1:
        print(part)
        print()
        print("uh oh")
    r = a
    a = sym(''.join(line[0] for line in lines))
    for c in range(len(lines[0])):
        line = ''.join(line[c] for line in lines)
        a = a.intersection(sym(line))
    # print(f"a={a}")
    if len(a) > 1:
        print("columns")
        print(part)
        print(f"a={a}")
        print()
        print("uh oh")
    return (r, a)

sm = 0
for part in parts:
    
    lines = part.splitlines()
    done = False
    (origr, origc) = find_refl(lines)
    print()
    print(origr, origc)
    for r in range(len(lines)):
        if done:
            break
        for c in range(len(lines[0])):
            new = deepcopy(lines)
            if lines[r][c] == "#":
                new[r] = lines[r][:c] + "." + lines[r][c+1:]
            if lines[r][c] == ".":
                new[r] = lines[r][:c] + "#" + lines[r][c+1:]
            # for row in new:
            #     print(row)
            # print()
            (rr, rc) = find_refl(new)
            # print(rr, rc)
            rr = rr.difference(origr)
            rc = rc.difference(origc)
            # print(rr, rc)
            if len(rr) != 0 or len(rc) != 0:
                sm += sum(rr) + 100*sum(rc) 
                print(f"found at {r} {c}")
                done = True
                break
            print()

    
    # (r, a) = find_refl(part)
    # for s in list(r):
    #     sm += s
    # for s in list(a):
    #     sm += 100*s

    # print(sm)
    # print("-------------------")

print(sm)

#22257
#23257 too low