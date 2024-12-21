# using aoc_template.py
# from https://realpython.com/python-advent-of-code/
# Day 6: Guard Gallivant
# 2024

import pathlib
import sys
import re
from collections import defaultdict
from functools import cmp_to_key

def parse(puzzle_input):
    """Parse input."""
    lines = puzzle_input.split('\n')
    lines2 = []
    for l in lines:
        lines2.append(list(l))
    for r in range(len(lines)):
        line = lines[r]
        for c in "<^>v":
            idx = line.find(c)
            if idx != -1:
                return lines2, r, idx, c
    print("error - guard not found")
    return lines2, -1, -1

def isValid(r, c, lines):
    return 0 <= r < len(lines) and 0 <= c < len(lines[0])

def countX(lines):
    count = 0
    for l in lines:
        count += l.count('x')
    return count

def part1(data):
    """Solve part 1."""
    lines, r, c, guard = data
    guardIdx = "<^>v".find(guard)
    dirs = {'<' : (0, -1), '^' : (-1, 0), '>' : (0, 1), 'v' : (1, 0)}
    dir = dirs[guard]
    r, c = (r + dir[0], c + dir[1])
    while isValid(r, c, lines):
        if lines[r][c] == '#':
            guardIdx = (guardIdx + 1) % 4
            guard = "<^>v"[guardIdx]
            r, c = (r - dir[0], c - dir[1]) # reset
        else:
            lines[r][c] = 'x'
        dir = dirs[guard]
        r, c = (r + dir[0], c + dir[1])
    return countX(lines)

def copyGrid(lines):
    grid = []
    for l in lines:
        # okay to write over guard location '^' or 'v' or whatever
        r_copy = l.copy()
        row_copy = [x if (x == '#' or x.isdigit()) else '0' for x in r_copy]
        grid.append(row_copy)
    return grid


def loopFound(r, c, guard, grid):
    guardIdx = "<^>v".find(guard)
    dirs = {'<' : (0, -1), '^' : (-1, 0), '>' : (0, 1), 'v' : (1, 0)}
    dir = dirs[guard]
    original_row_col = (r, c)
    original_guard = guard
    visited = set()
    visited.add((r, c, dir))
    r, c = r + dir[0], c + dir[1]
    while isValid(r, c, grid):
        if grid[r][c] == '#':
            guardIdx = (guardIdx + 1) % 4
            guard = "<^>v"[guardIdx]
            r, c = (r - dir[0], c - dir[1]) # reset
        else:
            grid[r][c] = 'x'
        dir = dirs[guard]
        r, c = (r + dir[0], c + dir[1])
        #if (r, c) == original_row_col and original_guard == guard:
        if (r, c, dir) in visited:
            return True
        visited.add((r, c, dir))
    return False

def printGrid(grid):
    for row in grid:
        for c in row:
            print(c, end='')
        print('\n', end='')
    print('\n', end='')

def part2(data): # 1617 too low, 1767 is too high, 1670 right answer
    """Solve part 2."""
    lines, r, c, guard = data
    guardIdx = "<^>v".find(guard)
    dirs = {'<' : (0, -1), '^' : (-1, 0), '>' : (0, 1), 'v' : (1, 0)}
    dir = dirs[guard]
    rNext, cNext = (r + dir[0], c + dir[1])
    lines = copyGrid(lines)
    """
    make copy of lines
    put # in next position
    trace guard around - does it intersect?
      if so, print location of # and add to count
    move guard, store anded direction
    """
    count = 0
    blockers = set()
    already_visited = set()
    already_visited.add((r,c))
    while isValid(rNext, cNext, lines):
        if lines[rNext][cNext] != '#':
            if not (rNext, cNext) in  already_visited:
                grid = copyGrid(lines)
                grid[rNext][cNext] = '#'
                if loopFound(r, c, guard, grid):
                    count += 1
                    blockers.add((r, c))
                #updateBitValue(c, guardIdx, lines, r)
            r, c = rNext, cNext
            already_visited.add((r,c))
        else:
            guardIdx = (guardIdx + 1) % 4
            guard = "<^>v"[guardIdx]
        dir = dirs[guard]
        rNext, cNext = (r + dir[0], c + dir[1])
        # print(r, c)
    #print ("size: ", len(blockers))
    return count


def updateBitValue(c, guardIdx, lines, r):
    num = ord(lines[r][c]) - ord('0')
    bit_value = pow(2, guardIdx)
    num = num | bit_value
    lines[r][c] = chr(num + ord('0'))


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
