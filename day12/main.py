#!/usr/bin/env python3

import sys
from collections import defaultdict
from functools import cache
from itertools import product
import math
# from numpy import np

with open(sys.argv[1]) as f:
    data = f.read().strip()
lines = data.split("\n")
print("------------------------------------------------------")

print(lines)



sm = 0
for line in lines:
    n = 0
    for ch in line.split()[0]:
        if ch == "?":
            n += 1

    arr = list(map(int, line.split()[1].split(',')))
    rest = line.split()[0]
    print()
    cnt = 0
    for comb in product([True, False], repeat=n):
        i = 0
        res = ""
        for ch in rest:
            if ch == "?":
                if comb[i]:
                    res += "."
                else:
                    res += "#"
                i += 1
            else:
                res += ch
        res += "."
        real_arr = []
        cur = 0
        for ch in res:
            if ch == ".":
                if cur != 0:
                    real_arr.append(cur)
                    cur = 0
            else:
                cur += 1
        if arr == real_arr:
            cnt += 1
            
    print(cnt)
    sm += cnt

print(sm)