#!/usr/bin/env python3

import sys
from collections import defaultdict

with open(sys.argv[1]) as f:
    lines = [line.strip() for line in f.readlines()]
lines.append("")
print("------------------------------------------------------")


# stos = defaultdict(lambda x: x)
def p1():
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

    print(seeds)
    print(min(seeds))

"""
def p2():
    def intersection(range1, range2):
        s = sorted([range1, range2], key=lambda tpl: tpl[0])
        if s[0][1] > s[1][1]:
            return ((s[0][0], s[1][0]), s[1], (s[1][1]+1, s[0][1]))
        elif s[0][1] == s[1][1]:
            return ((s[0][0], s[1][0]), s[1], None)
        elif s[0][1] <= s[1][0]:
            return None
        else:
            return ((s[0][0], s[1][0]), (s[1][0], s[0][1]), (s[0][1]+1, s[1][1]))


    def mp(range_maps, ranges):
        new_ranges = []
        
        while len(ranges) != 0:
            rng = ranges.pop()
            # start, end = rng
            is_found = False
            for (start_end, start_from, step) in range_maps:
                inters= intersection(rng, (start_from, start_from+step))
                def mp_val(v):
                    return start_end+v-start_from
                
                if inters:
                    left, mid, right = inters
                    # print()
                    # print(rng)
                    # print((start_from, start_from+step))
                    # print(inters)
                    # print()
                    new_ranges.append((mp_val(mid[0]), mp_val(mid[1])))
                    if mid == rng:
                        pass
                    elif intersection(rng, left):
                        ranges.append(left)
                    elif right and intersection(rng, right):
                        ranges.append(right)
                    
                    is_found = True
            if not is_found:
                new_ranges.append(rng)
        
        return new_ranges


    orig_seeds = [int(p) for p in lines[0][7:].split()]
    cur_seeds = []
    for i in range(0, len(orig_seeds), 2):
        first = orig_seeds[i]
        last = first+orig_seeds[i+1]
        seed_range = (first, last)
        cur_seeds.append(seed_range)
    # print(cur_seeds)


    cur_line = 2
    cur_ranges = []
    while cur_line < len(lines):
        line = lines[cur_line]
        cur_line += 1

        if line == "":
            new_seeds = []
            print(len(cur_seeds))
            for seeds in cur_seeds:
                # print(f"seeds={seeds}")

                new = mp(cur_ranges, [seeds])
                for n in new:
                    new_seeds.append(n)
                # print(f"new_seeds={new_seeds}")
            cur_seeds = new_seeds

            cur_ranges = []
        elif not line[0].isdigit():
            continue
        else:
            cur_ranges.append(tuple(map(int, line.split())))
        
    print(min(t[0] for t in cur_seeds))
"""
p1()
# p2()

# def mp(range_maps, init_values):
#     l = []

#     for v in init_values:
#         is_found = False
#         for (start_end, start_from, step) in range_maps:
#             if start_from <= v < start_from + step:
#                 l.append(start_end + v-start_from)
#                 is_found = True
#         if not is_found:
#             l.append(v)
    
#     return l

# orig_seeds = [int(p) for p in lines[0][7:].split()]
# points_of_interest = []
# m = 10**15
# for i in range(0, len(orig_seeds), 2):
#     poi = []
#     poi.append(orig_seeds[i])
#     poi.append(orig_seeds[i]+orig_seeds[i+1])

#     mappings = []
#     cur_line = 2
#     cur_ranges = []
#     while cur_line < len(lines):
#         line = lines[cur_line]
#         cur_line += 1

#         if line == "":
#             mappings.append(cur_ranges)
#             cur_ranges = []
#         elif not line[0].isdigit():
#             continue
#         else:
#             cur_ranges.append(tuple(map(int, line.split())))

#     print(f"poi={poi}")
#     for mapping in mappings:
#         new_poi = poi
#         for i in range(len(poi)-1):
#             for (dst, src, n) in mapping:
#                 if poi[i] < src < poi[i+1]:
#                     new_poi.append(src)
#                     new_poi.append(src-1)
#                 if poi[i] < dst < poi[i+1]:
#                     new_poi.append(dst)
#                     new_poi.append(dst+1)
            
#         new_poi.sort()
#         print(new_poi)
#         print(len(poi))
#         poi = mp(mapping, new_poi)

#     m = min(min(poi), m)
# print(m)