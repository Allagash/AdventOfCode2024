# using aoc_template.py
# from https://realpython.com/python-advent-of-code/
# Day 3, Mull It Over
# 2024

import pathlib
import sys
import re
from collections import defaultdict

def parse(puzzle_input):
    """Parse input."""
    lines = puzzle_input.split('\n')
    return lines



def part1(data):
    """Solve part 1."""
    result = 0
    #print(data)
    for line in data:
        muls = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", line)
        for m in muls:
            nums = re.findall("[0-9]{1,3}", m)
            result += int(nums[0]) * int(nums[1])
        #print(muls)
    return result

def part2(data): #  111972528 too high
    """Solve part 2."""
    result = 0
    #print(data)
    doit = True
    for line in data:
        instructions = re.findall("(don't\(\)|do\(\)|mul\([0-9]{1,3}\,[0-9]{1,3}\))", line)
        # print(instructions)
        for i in instructions:
            if i == "do()":
                doit = True
            elif i == "don't()":
                doit = False
            elif doit:
                nums = re.findall("[0-9]{1,3}", i)
                result += int(nums[0]) * int(nums[1])

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
