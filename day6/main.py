#!/usr/bin/env python3

import sys
from collections import defaultdict

with open(sys.argv[1]) as f:
    lines = [line.strip() for line in f.readlines()]
lines.append("")
print("------------------------------------------------------")


def test(n, ms):
    sm = 0
    return n*(ms-n)

_, *times = lines[0].split()
_, *distance = lines[1].split()
times = [int(''.join(times))]
distance = [int(''.join(distance))]
print(times, distance)


p = 1
for i in range(len(times)):
    ms = int(times[i])
    d = int(distance[i])
    valid = []
    for n in range(0, ms+1):
        if test(n, ms) > d:
            valid.append(n)
    
    p*= len(valid)
    # print(valid)

print(p)

