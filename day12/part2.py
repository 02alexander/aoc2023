#!/usr/bin/env python3

import sys
from collections import defaultdict
from functools import cache
from itertools import product, permutations
import math

with open(sys.argv[1]) as f:
    data = f.read().strip()
lines = data.split("\n")
print("------------------------------------------------------")

@cache
def solve(s, arr):
    if len(s) == 0 and len(arr) == 0:
        return 1
    elif len(s) == 0:
        return 0

    if s[0] == ".":
        return solve(s[1:], arr)
    else:
        sm = 0
        if s[0] == "?":
            sm += solve(s[1:], arr) # set ? to .

        if len(arr) != 0 and len(s)-arr[0] >= 0:
            if all(c != "." for c in s[:arr[0]]):
                if s[arr[0]] != "#":
                    sm += solve(s[arr[0]+1:], arr[1:])

        return sm

    
sm = 0
for line in lines:
    rest, arr = line.split()
    arr = tuple(map(int, arr.split(',')))
    s = solve(rest+ ("?"+rest)*4 +".", tuple(list(arr)*5))
    sm += s

print(sm)