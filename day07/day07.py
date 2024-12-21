# using aoc_template.py
# from https://realpython.com/python-advent-of-code/
# Day 7: Bridge Repair
# 2024

import pathlib
import sys
import re
from collections import defaultdict
from functools import cmp_to_key

def parse(puzzle_input):
    """Parse input."""
    lines = puzzle_input.split('\n')
    ops = []
    sums = []
    for l in lines:
        input = l.split(':')
        sums.append(int(input[0]))
        ops.append([int(x) for x in input[1].split()])
    #print(sums)
    #print(ops)
    return sums, ops


def part1(data):
    """Solve part 1."""
    sums, ops = data
    count = 0
    for i in range(len(sums)):
        sum = sums[i]
        op_list = ops[i]
        num_bits = len(op_list) - 1
        for j in range(pow(2, num_bits)):
            result = op_list[0]
            for k in range(num_bits):
                if (j & pow(2, k)) == 0:
                    result += op_list[k + 1]
                else:
                    result *= op_list[k + 1]
            if result == sum:
                count += sum
                break
    return count

def getNextTrinaryNum(digits):
    digits[0] += 1
    carry = 0
    digit = 1
    if digits[0] > 2:
        digits[0] = 0
        carry = 1
    while carry != 0 and digit < len(digits):
        digits[digit] += 1
        if digits[digit] > 2:
            digits[digit] = 0
            carry = 1
        else:
            carry = 0
        digit += 1
    return digits

def part2(data): # 1617 too low, 1767 is too high, 1670 right answer
    """Solve part 2."""
    sums, ops = data
    count = 0
    for i in range(len(sums)):
        sum = sums[i]
        op_list = ops[i]
        num_bits = len(op_list) - 1
        bits = [0] * num_bits
        for j in range(pow(3, num_bits)):
            result = op_list[0]
            for k in range(num_bits):
                if bits[k] == 0:
                    result += op_list[k + 1]
                elif bits[k] == 1:
                    result *= op_list[k + 1]
                else:
                    result = int(str(result) + str(op_list[k + 1]))
            if result == sum:
                count += sum
                break
            getNextTrinaryNum(bits)
    return count

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
