# using aoc_template.py
# from https://realpython.com/python-advent-of-code/
# Day 10: Hoof It
# 2024

import pathlib
import sys
import re
from collections import defaultdict
from functools import cmp_to_key

def parse(puzzle_input):
    """Parse input."""
    return puzzle_input.split('\n')

def valid_pos(p, data):
    return 0 <= p[0] < len(data) and 0 <= p[1] < len(data[0])

def get_paths(z, data):
    height = int(data[z[0]][z[1]])
    if height == 9:
        return {(z)}
    # get all surrounding possibilities
    queue = []
    for p in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        next = (z[0] + p[0], z[1] + p[1])
        if valid_pos(next, data) and data[next[0]][next[1]].isdigit() and int(data[next[0]][next[1]]) == height + 1:
            queue.append(next)
    result = set()
    for n in queue:
        result.update(get_paths(n, data))
    return result

def get_paths2(z, data):
    height = int(data[z[0]][z[1]])
    if height == 9:
        return 1
    # get all surrounding possibilities
    queue = []
    for p in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        next = (z[0] + p[0], z[1] + p[1])
        if valid_pos(next, data) and data[next[0]][next[1]].isdigit() and int(data[next[0]][next[1]]) == height + 1:
            queue.append(next)
    result = 0
    for n in queue:
        result += get_paths2(n, data)
    return result

def part1(data):
    """Solve part 1."""
    zeros = []
    for r in range(len(data)):
        line = data[r]
        for c in range(len(line)):
            if line[c] == '0':
              zeros.append((r, c))
    result = 0
    for z in zeros:
        result += len(get_paths(z, data))
    return result


def part2(data):
    """Solve part 2."""
    zeros = []
    for r in range(len(data)):
        line = data[r]
        for c in range(len(line)):
            if line[c] == '0':
              zeros.append((r, c))
    result = 0
    for z in zeros:
        result += get_paths2(z, data)
    return result


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
