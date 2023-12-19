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

def test_rule(val, rule):
    if ">" in rule:
        v = val[rule.split(">")[0]]
        return v > int(rule.split('>')[1])
    elif "<" in rule:
        v = val[rule.split("<")[0]]
        return v < int(rule.split('<')[1])
    else:
        print("uh oh")
        

lines = [line.strip() for line in data.splitlines()]

works = defaultdict(list)

i = 0
for line in lines:
    if line.strip() == "":
        break
    i += 1
    id, other = line.split("{")
    rules = other[:-1].split(',')
    for rule in rules:
        if ":" in rule:
            parts = rule.split(":")
            works[id].append((True, (parts[0], parts[1])))
        else:
            works[id].append((False, rule))

print(works)

sm = 0
for line in lines[i+1:]:
    stuff = line[1:-1].split(",")
    val = {}
    for part in stuff:
        var, v = part.split("=")
        val[var] = int(v)

    cur = "in"
    done = False
    print(val)
    while not done:
        if cur == "A":
            sm += sum(val.values())
            break
        elif cur == "R":
            break
        
        rules = works[cur]
        for (is_rule, rule) in rules:
            if not is_rule:
                cur = rule
                break
            if is_rule and test_rule(val, rule[0]):
                cur = rule[1]
                break



    print("-------------")        


    print(val)

print(sm)