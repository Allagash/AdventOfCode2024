# using aoc_template.py
# from https://realpython.com/python-advent-of-code/
# Day 2, Red-Nosed Reports
# 2024

import pathlib
import sys
from collections import defaultdict

def parse(puzzle_input):
    """Parse input."""
    lines = puzzle_input.split('\n')
    list_of_data = []
    for line in lines:
        list_of_data.append([int(x) for x in line.split()])
    return list_of_data

def reportOK(reports):
    increase = reports[0] < reports[1]
    for i in range(len(reports) - 1):
        if increase != (reports[i] < reports[i + 1]):
            return False
        diff = abs((reports[i] - reports[i+1]))
        if diff < 1 or diff > 3:
            return False
    return True


def part1(data):
    """Solve part 1."""
    result = 0
    #print(data)
    for line in data:
        if reportOK(line):
            result = result + 1
    return result

def part2(data):
    """Solve part 2."""
    result = 0
    #print(data)
    for line in data:
        if reportOK(line):
            result = result + 1
        else:
            for i in range(len(line)):
                l2 = line.copy()
                l2.pop(i)
                if reportOK(l2):
                    result = result + 1
                    break

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
