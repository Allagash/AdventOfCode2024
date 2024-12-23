# using aoc_template.py
# from https://realpython.com/python-advent-of-code/
# Day 11: Plutonian Pebbles
# 2024

import pathlib
import sys
import re
from collections import defaultdict
from functools import cmp_to_key

def parse(puzzle_input):
    """Parse input."""
    return [int(x) for x in puzzle_input.split()]


def part1(data, num_blinks):
    """Solve part 1."""
    result = 0
    for i in range(num_blinks):
        #print(i)
        next = []
        for d in data:
            if d == 0:
                next.append(1)
            elif len(str(d)) % 2 == 0:
                s = str(d)
                half_len = len(str(d)) // 2
                first = s[:half_len]
                second = s[half_len:]
                next.append(int(first))
                next.append(int(second))
            else:
                next.append(2024 * d)
        data = next
    #print(data)
    return len(data)

cache = dict()

def get_blink(num):
    next = []
    if num == 0:
        next.append(1)
    elif len(str(num)) % 2 == 0:
        s = str(num)
        half_len = len(str(num)) // 2
        first = s[:half_len]
        second = s[half_len:]
        next.append(int(first))
        next.append(int(second))
    else:
        next.append(2024 * num)
    return next

def get_result(num, num_blinks):
    if num_blinks == 0:
        return 1
    if (num, num_blinks) in cache:
        return cache[(num, num_blinks)]

    next = get_blink(num)
    result = 0
    for n in next:
        result += get_result(n, num_blinks - 1)
    cache[(num, num_blinks)] = result
    return result

def part2(data, num_blinks):
    result = 0
    for d in data:
        result += get_result(d, num_blinks)
    return result



def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    data2 = parse(puzzle_input)
    solution1 = part1(data, 25)
    solution2 = part2(data2, 75)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
