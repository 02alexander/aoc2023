#!/usr/bin/env python3

import sys
from collections import defaultdict
from functools import cache
from itertools import product
import math
from copy import deepcopy
# from numpy import np

with open(sys.argv[1]) as f:
    data = f.read().strip()
# lines = data.splitlines()

def hash(s):
    cur = 0
    for c in s:
        n = ord(c)
        cur += n
        cur *= 17
        cur = cur % 256
    return cur

def removen(label, n):
    for i in range(len(boxes[n])):
        if boxes[n][i][0] == label:
            del boxes[n][i]
            break

def add(label, val, n):
    for i in range(len(boxes[n])):
        if boxes[n][i][0] == label:
            boxes[n][i] = (lbl, val)
            return
    boxes[n].append((lbl, val))


boxes = [[] for _ in range(256)]

sm = 0 
for part in data.split(","):
    h = hash(part)
    if "=" in part:
        lbl, to = part.split("=")
        # print("hash lbl = ", hash(lbl))
        add(lbl, int(to), hash(lbl))
    elif "-" in part:
        lbl, *other = part.split("-")
        # print("hash lbl = ", hash(lbl))
        removen(lbl, hash(lbl))
    # for i in range(len(boxes)):
    #     if len(boxes[i]) != 0:
    #         print(i, boxes[i])
    # print()
    sm += h
    # print(h)

tot_pow = 0
for i in range(len(boxes)):
    for (k, (lbl, f)) in enumerate(boxes[i]):
        tot_pow += (1+i)*(k+1)*f
print(tot_pow)

print(sm)
