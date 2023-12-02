#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()
# numbs = list(map(int, lines))

def p1():
    sm = 0
    for (gi, line) in enumerate(lines):
        parts = line.split()
        rest = parts[2:]
        possible = True
        limits = [12, 13, 14]
        for i in range(0, len(rest), 2):
            n = int(rest[i])
            color = rest[i+1]
            if color[-1] == ',' or color[-1] == ";":
                color = color[:-1]
            idx = 0
            if color == "green":
                idx = 1
            elif color == "blue":
                idx = 2
            if n > limits[idx]:
                possible = False
        if possible:
            sm += gi+1
    print(sm)



def p2():
    sm = 0
    for (gi, line) in enumerate(lines):
        parts = line.split()
        rest = parts[2:]
        # possible = True
        limits = [-1, -1, -1]
        for i in range(0, len(rest), 2):
            n = int(rest[i])
            color = rest[i+1]
            if color[-1] == ',' or color[-1] == ";":
                color = color[:-1]
            idx = 0
            if color == "green":
                idx = 1
            elif color == "blue":
                idx = 2
            limits[idx] = max(n, limits[idx])
        print(limits)
        sm += limits[0]*limits[1]*limits[2]

    print(sm)  

# p1()
p2()