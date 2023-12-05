#!/usr/bin/env python3

import sys
from collections import defaultdict

with open(sys.argv[1]) as f:
    lines = [line.strip() for line in f.readlines()]
lines.append("")
print("------------------------------------------------------")


def mp(range_maps, init_values):
        l = []

        for v in init_values:
            is_found = False
            for (start_end, start_from, step) in range_maps:
                if start_from <= v < start_from + step:
                    l.append(start_end + v-start_from)
                    is_found = True
            if not is_found:
                l.append(v)
        
        return l

def p1():
    orig_seeds = [int(p) for p in lines[0][7:].split()]
    seeds = orig_seeds

    cur_line = 2
    cur_ranges = []
    while cur_line < len(lines):
        line = lines[cur_line]
        cur_line += 1

        if line == "":
            seeds = mp(cur_ranges, seeds)
            cur_ranges = []
        elif not line[0].isdigit():
            continue
        else:
            cur_ranges.append(tuple(map(int, line.split())))

    return min(seeds)

def inverse_mapping(range_maps):
    return [ (tpl[1], tpl[0], tpl[2]) for tpl in range_maps ]

def p2():

    mappings = []
    cur_line = 2
    cur_ranges = []
    while cur_line < len(lines):
        line = lines[cur_line]
        cur_line += 1

        if line == "":
            mappings.append(cur_ranges)
            cur_ranges = []
        elif not line[0].isdigit():
            continue
        else:
            cur_ranges.append(tuple(map(int, line.split())))

    inv_mpings = [inverse_mapping(mp) for mp in mappings][::-1]


    orig_seeds = [int(p) for p in lines[0][7:].split()]
    points_of_interest = []
    m = 10**15
    for i in range(0, len(orig_seeds), 2):
        poi = []
        poi.append(orig_seeds[i])
        poi.append(orig_seeds[i]+orig_seeds[i+1])

        for mapping in mappings:
            new_poi = poi
            for k in range(len(poi)-1):
                for (dst, src, n) in mapping:
                    if poi[k] < src < poi[k+1]:
                        new_poi.append(src)
                        new_poi.append(src-1)
                    if poi[k] < dst < poi[k+1]:
                        new_poi.append(dst)
                        new_poi.append(dst+1)
                
            new_poi.sort()
            poi = mp(mapping, new_poi)

        for p in poi:
            orig = p
            for inv_mp in inv_mpings:
                p = mp(inv_mp, [p])[0]
            if orig_seeds[i] <= p < orig_seeds[i]+orig_seeds[i+1]:
                m = min(m, orig)

    return m

print(p1())
print(p2())