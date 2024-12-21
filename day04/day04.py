# using aoc_template.py
# from https://realpython.com/python-advent-of-code/
# Day 4, Ceres Search
# 2024

import pathlib
import sys
import re
from collections import defaultdict

def parse(puzzle_input):
    """Parse input."""
    lines = puzzle_input.split('\n')
    return lines

def foundWord(r, c, rInc, cInc, data):
    word = "XMAS"
    for l in word:
        if r < 0 or r >= len(data) or c < 0 or c >= len(data[0]):
            return False
        if data[r][c] != l:
            return False
        r += rInc
        c += cInc
    return True

def numSolutions(row, col, data):
    count = 0
    for rInc in range(-1, 2): # -1, 0, 1
        for cInc in range(-1, 2):  # -1, 0, 1
            if foundWord(row, col, rInc, cInc, data):
                count += 1
    return count

def foundOneX() :
    return 0


def invalidPos(r, c, data):
    return  r < 0 or r >= len(data) or c < 0 or c >= len(data[0])

def xmasFound(r, c, data):
    if invalidPos(r, c, data): # don't need
        return 0
    if data[r][c] != 'A':
        return 0
    # -1 -1, -1 1, 1 1, 1 -1
    # MMSS, MSSM,
    pos = [(r -1, c-1), (r -1, c+ 1), (r + 1, c+ 1), (r + 1, c-1)]
    seq = "MMSS"
    for i in range(4):
        if 'M' == data[pos[0][0]][pos[0][1]] and \
            'M' == data[pos[1][0]][pos[1][1]] and \
            'S' == data[pos[2][0]][pos[2][1]] and \
            'S' == data[pos[3][0]][pos[3][1]]:
            return 1
        p = pos.pop(0)
        pos.append(p)
    return 0

def part1(data):
    """Solve part 1."""
    result = 0
    for r in range(len(data)):
        for c in range(len(data[0])):
            result += numSolutions(r, c, data)
    return result

def part2(data):
    """Solve part 2."""
    result = 0
    for r in range(1, len(data) - 1):
        for c in range(1, len(data[0]) - 1):
            result += xmasFound(r, c, data)
    return result

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
