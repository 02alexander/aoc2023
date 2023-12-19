#!/usr/bin/env python3

import sys
from collections import defaultdict
from functools import cache
from itertools import product, permutations
import math

with open(sys.argv[1]) as f:
    data = f.read().strip()
lines = data.split("\n")

@cache
def solve(s, arr):
    sm = 0
    if len(s) == 0 and len(arr) == 0: return 1
    elif len(s) == 0: return 0
    elif s[0] in [".", "?"]: sm += solve(s[1:], arr)
    if len(arr) != 0 and len(s)-arr[0] >= 0 and all(c != "." for c in s[:arr[0]]) and s[arr[0]] != "#":
        sm += solve(s[arr[0]+1:], arr[1:])
    return sm

sm = 0
for line in lines:
    rest, arr = line.split()
    arr = tuple(map(int, arr.split(',')))
    s = solve(rest+ ("?"+rest)*4 +".", tuple(list(arr)*5))
    sm += s

print(sm)

#4500070301581