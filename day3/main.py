#!/usr/bin/env python3

import sys

lines = [line.strip()+"." for line in sys.stdin.readlines()]
# numbs = list(map(int, lines))


star_cords = set()
for (row, line) in enumerate(lines):
    for (col, ch) in enumerate(line):
        if not ch.isdigit() and ch != ".":
            star_cords.add((row, col))

print(star_cords)

part_numbers = {}

sm = 0
part_number_id = 0
for (row, line) in enumerate(lines):
    cur_digit = ""
    is_adj = False
    for (col, ch) in enumerate(line):
        if ch.isdigit():
            cur_digit += ch

        delta = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
        for (dr, dc) in delta:
            if (row+dr, col+dc) in star_cords and ch.isdigit() and cur_digit != "":
                is_adj = True

        if not ch.isdigit():
            if cur_digit != "" and is_adj:
                sm += int(cur_digit)
                for dc in range(len(cur_digit)):
                    print((row, col-dc-1))
                    part_numbers[(row, col-dc-1)] = (part_number_id, int(cur_digit))
                part_number_id += 1
                print(cur_digit)
            cur_digit = ""
            is_adj = False

print(star_cords)
print(sm)

cnt = 0
for (row, line) in enumerate(lines):
    for (col, ch) in enumerate(line):
        if ch == "*":
            delta = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
            parts = set()
            for (dr, dc) in delta:
                if (row+dr, col+dc) in part_numbers:
                    parts.add(part_numbers[(row+dr, col+dc)])
            # print(parts)
            if len(parts) == 2:
                m = 1
                for (id, n) in parts:
                    m *= n
                    # cnt += n
                # print(m)
                cnt += m
                continue
        
            # star_cords.add((row, col))
print(cnt)
