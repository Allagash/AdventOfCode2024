# using aoc_template.py
# from https://realpython.com/python-advent-of-code/
# Day 1, Historian Hysteria
# 2024

import pathlib
import sys
from collections import defaultdict

def parse(puzzle_input):
    """Parse input."""
    lines = puzzle_input.split('\n')
    list_of_pairs = []
    for line in lines:
        list_of_pairs.append(line.split())
    return list_of_pairs


def part1(data):
    """Solve part 1."""
    result = 0
    # print(data)
    list1 = []
    list2 = []
    for line in data:
        list1.append(int(line[0]))
        list2.append(int(line[1]))
    list1.sort()
    list2.sort()
    for i in range(len(list1)):
        result += abs(list1[i] - list2[i])
    return result

def part2(data):
    """Solve part 2."""
    result = 0
    list1 = []
    list2 = []
    list2Count = defaultdict(int)
    for line in data:
        list1.append(int(line[0]))
        num2 = int(line[1])
        list2.append(num2)
        list2Count[num2] = list2Count[num2] + 1
    #print(list2Count)
    for num in list1:
        result += num * list2Count[num]

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
