#!/usr/bin/env python3

import z3
import sys
import numpy as np

with open(sys.argv[1]) as f:
    data = f.read().strip()
lines = [line.strip() for line in data.splitlines()]

flakes = []

for line in lines:
    line = line.replace(",", "")
    p, v = line.split("@")
    p = list(map(int, p.split()))
    v = list(map(int, v.split()))
    flakes.append((np.array(p),np.array(v)))

px = z3.Real("px")
py = z3.Real("py")
pz = z3.Real("pz")
vx = z3.Real("vx")
vy = z3.Real("vy")
vz = z3.Real("vz")

s = z3.Solver()

ts = []
for (i, (p, v)) in enumerate(flakes):
    t = z3.Real("t" + str(i))
    s.add(px + vx*t == p[0] + v[0]*t)
    s.add(py + vy*t == p[1] + v[1]*t)
    s.add(pz + vz*t == p[2] + v[2]*t)
    ts.append(t)

s.check()
m = s.model()

p = [ int(str(m[p])) for p in [px, py, pz] ]
print(sum(p))
