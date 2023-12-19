#!/usr/bin/env python3

import re
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
keypoints = defaultdict(list)

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
            key, val = re.split("<|>", parts[0])
            keypoints[key].append(int(val))
            works[id].append((True, (parts[0], parts[1])))
        else:
            works[id].append((False, rule))

def limit_range(rng, val, lt):
    start, end = rng
    if lt:
        if val <= start:
            return (start, start)
        else:
            end = min(val, end)
    else:
        if val >= end:
            return (end, end)
        else:
            start = max(val, start)
    return (start, end)

def in_range(rng, val):
    start, end = rng
    return val >= start and val < end

results = []

def process(cur, cur_ranges):

    cnt = 0
    if cur == "A":
        cnt += math.prod(end-start for (start, end) in cur_ranges.values() )
    elif cur == "R":
        return 0
    
    rules = works[cur]
    for (is_rule, rule) in rules:
        if not is_rule:
            cnt += process(rule, cur_ranges)
        else:
            rule, dst = rule
            var, v = re.split("<|>", rule)

            if cur_ranges[var] is None:
                continue

            v = int(v)
            if "<" in rule:
                new_ranges = deepcopy(cur_ranges)
                new_ranges[var] = limit_range(new_ranges[var], v, True)
                cnt += process(dst, new_ranges)


                cur_ranges[var] = limit_range(cur_ranges[var], v, False)


            if ">" in rule:
                new_ranges = deepcopy(cur_ranges)
                new_ranges[var] = limit_range(new_ranges[var], v+1, False)
                cnt += process(dst, new_ranges)

                cur_ranges[var] = limit_range(cur_ranges[var], v+1, True)


    return cnt

np = lambda x: list(range(len(keypoints[x])-1))

vars = ["x", "m", "a", "s"]

ranges = {}

for var in vars:
    ranges[var] = (1, 4001)

print(process("in", ranges))