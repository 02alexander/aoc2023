#!/usr/bin/env python3

import sys
from collections import defaultdict
from itertools import combinations, permutations, product
from functools import cache

with open(sys.argv[1]) as f:
    lines = [line.strip() for line in f.readlines()]
lines.append("")
print("------------------------------------------------------")

def is_type(cards, type):
    d = defaultdict(int)
    for c in cards:
        d[c] += 1
    cnts = sorted(list(d.items()), key=lambda x: x[1], reverse=True)
    for i in range(len(type)):
        if cnts[i][1] != type[i]:
            return False
    return True

@cache
def ranking(cards):
    j_pos = []
    for (i, c) in enumerate(cards):
        if c == "J":
            j_pos.append(i)
    combs = list(product(["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K","A"], repeat=len(j_pos)))
    highest = raw_ranking(cards)
    for comb in combs:
        res =""
        for (i, c) in enumerate(cards):
            if i in j_pos:
                res += comb[j_pos.index(i)]
            else:
                res += c
        highest = max(raw_ranking(res), highest)
    return highest

def raw_ranking(cards):
    r = None
    if is_type(cards, [5]):
        r = 6
    elif is_type(cards, [4, 1]):
        r = 5
    elif is_type(cards, [3, 2]):
        r = 4
    elif is_type(cards, [3, 1, 1]):
        r = 3
    elif is_type(cards, [2, 2, 1]):
        r = 2
    elif is_type(cards, [2, 1, 1, 1]):
        r = 1
    elif is_type(cards, [1, 1, 1, 1, 1]):
        r = 0
    else:
        print("uh oh")
    return r

def cstrength(cards):
    res = ""
    for c in cards:
        n = None
        if c.isdigit():
            n = int(c)
        elif c == "T":
            n = 10
        elif c == "J":
            n = 1
        elif c == "Q":
            n = 12
        elif c == "K":
            n = 13
        elif c == "A":
            n = 14
        else:
            print("uh oh")
        res += chr(ord('a')+n)
    return res

cards = []

score = {}
for line in lines:
    if line == "":
        continue
    parts  = line.split()
    cards.append((parts[0], int(parts[1])))
    score[parts[0]] = int(parts[1])

c = sorted([(ranking(t[0]), cstrength(t[0]), t[0], t[1]) for t in cards])
sm = 0
for (i, (_, _, _, n)) in enumerate(c):
    sm += (i+1)*n
print(sm)

