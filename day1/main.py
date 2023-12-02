#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()
# numbs = list(map(int, lines))

sm = 0
for line in lines:
    line = line.strip()
    mp = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    res = ""
    i = 0
    first = -1
    for i in range(len(line)):
        if first != -1:
            break
        if line[i].isdigit():
            first = int(line[i])
            break
        for (k, v) in mp.items():
            if line[i:].startswith(k):
                first = v
                break
        
    larst = -1
    for i in range(len(line)-1, -1, -1):
        if larst != -1:
            break
        if line[i].isdigit():
            larst = int(line[i])
            continue
        for (k, v) in mp.items():
            if line[i:].startswith(k):
                larst = v
                break
    
    print(line)
    print(first, larst)
    sm += int(str(first)+str(larst))
        
print(sm)

    