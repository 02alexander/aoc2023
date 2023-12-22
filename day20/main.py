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


class Flip:
    def __init__(self, outs):
        self.state = False
        self.outs = outs

    
    def reset(self):
        self.state = False

    def activate(self, x, lbl):
        if not x:
            self.state = not self.state
            return self.state
        else:
            return None

class Conj:
    def __init__(self, outs):
        self.state = {}
        self.outs = outs
    
    def reset(self):
        self.state = False
    
    def activate(self, x, lbl):
        self.state[lbl] = x 

        # print("conj", list(self.state.items()))
        return not all(self.state.values())

cur_sig = []
broads = 0
mods = {}
start = None
wires = defaultdict(list)
for line in lines:
    line = line.replace(",", "")
    parts = line.split()
    if parts[0] == "broadcaster":
        broads = len(parts[2:])
        for part in parts[2:]:
            cur_sig.append(("broadcaster", False, part, ))
            # cur_sig[part] = False
        start = deepcopy(cur_sig)
    elif parts[0][0] == "%":
        src = parts[0][1:]
        dst = parts[2:]
        
        for d in dst:
            wires[d].append(src)
        # wires[src] = dst

        mods[src] = Flip(dst)

    elif parts[0][0] == "&":
        src = parts[0][1:]
        dst = parts[2:]
        for d in dst:
            wires[d].append(src)
        mods[src] = Conj(dst)


for lbl, value in mods.items():
    inps = wires[lbl]
    if type(value) == Conj:
        for inp in inps:
            value.activate(False, inp)



print("_"*20)

cnt_low = 0
cnt_high = 0
mn = 0

print(broads)

visited = set()
lps = defaultdict(list)
for n in range(10**3):
    cur_sigs = deepcopy(start)
    cnt_low += 1
    cnt_low += len(start)
    while len(cur_sigs) > 0:
        src, sig, lbl = cur_sigs[0]
        del cur_sigs[0]
        if lbl == "output":
            continue

                
        # print()
        # print(lbl, sig)
        if lbl not in mods:
            continue
        mod = mods[lbl]
        y = mod.activate(sig, src)
        if y is None:
            continue

        for out in mod.outs:
            if y:
                cnt_high += 1
            else:
                cnt_low += 1
            state = "low"
            if y:
                state = "high"
            # print(f'{lbl} -{state}-> {out}')
            cur_sigs.append((lbl, y, out))

    # print("--------------------------")

print(cnt_high*cnt_low)