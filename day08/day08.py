# using aoc_template.py
# from https://realpython.com/python-advent-of-code/
# Day 8: Resonant Collinearity
# 2024

import pathlib
import sys
import re
from collections import defaultdict
from functools import cmp_to_key

def parse(puzzle_input):
    """Parse input."""
    lines = puzzle_input.split('\n')
    cols = len(lines[0])
    rows = len(lines)
    locns = defaultdict(list)
    for r in range(rows):
        for c in range(cols):
            if lines[r][c] != '.':
                locns[lines[r][c]].append((r,c))
    return rows, cols, locns

def isValid(pt, rows, cols):
    return 0 <= pt[0] < rows and 0 <= pt[1] < cols


def part1(data):
    """Solve part 1."""
    antinodes = set()
    rows, cols, locns = data
    for f in list(locns.keys()):
        coords = locns[f]
        for c1 in coords: # does everything twice!
            for c2 in coords:
                if c1 == c2:
                    continue
                diff = (c2[0] - c1[0], c2[1] - c1[1])
                new0 = (c1[0] - diff[0], c1[1] - diff[1])
                if isValid(new0, rows, cols):
                    antinodes.add(new0)
                new1 = (c2[0] + diff[0], c2[1] + diff[1])
                if isValid(new1, rows, cols):
                    antinodes.add(new1)
    return len(antinodes)

def part2(data):
    """Solve part 2."""
    antinodes = set()
    rows, cols, locns = data
    for f in list(locns.keys()):
        coords = locns[f]
        for c1 in coords: # does everything twice!
            for c2 in coords:
                if c1 == c2:
                    continue
                diff = (c2[0] - c1[0], c2[1] - c1[1])
                new0 = (c1[0] - diff[0], c1[1] - diff[1])
                antinodes.add((c1[0], c1[1]))
                antinodes.add((c2[0], c2[1]))
                while isValid(new0, rows, cols):
                    antinodes.add(new0)
                    new0 = (new0[0] - diff[0], new0[1] - diff[1])
                new1 = (c2[0] + diff[0], c2[1] + diff[1])
                while isValid(new1, rows, cols):
                    antinodes.add(new1)
                    new1 = (new1[0] + diff[0], new1[1] + diff[1])
    return len(antinodes)

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    data2 = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data2)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
